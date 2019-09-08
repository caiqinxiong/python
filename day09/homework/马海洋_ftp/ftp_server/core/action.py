#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/3'

import os
from conf import settings
from core.file_read_write import FileReadWrite
from core.send_recv import Send_recv
from core.get_md5 import Get_md5
from core.log4 import logging


class Action(Send_recv):
    '''用户请求执行函数'''
    def __init__(self,sk):
        '''
        初始化函数
        :param sk: socket连接对象
        '''
        self.conn = sk
        self.name = None  # 登陆用户
        self.path = None  # 登陆后的默认家目录

    def __file_rename(self,file_name_path,file_md5_path):
        '''
        封装内部使用文件重命名函数
        :param file_name_path: 名称路径
        :param file_md5_path:  MD5文件名称路径
        :return:
        '''
        if  not os.path.exists(file_name_path):
            os.rename(file_md5_path, file_name_path)
        else:
            num = 1
            while True:
                file_name = os.path.basename(file_name_path)
                file,geshi = file_name.rsplit('.',maxsplit=1)
                new_name = '{0}_copy{1}.{2}'.format(file,num,geshi)
                new_path = os.path.join(self.path,new_name)
                if not os.path.exists(new_path): # 文件绝对路径不存在
                    os.rename(file_md5_path, new_path)
                    break
                else:
                    num+=1
                    continue

    def __md5_check(self,file_md5,file_md5_path):
        '''封装内部使用的文件MD5校验'''
        local_md5 = Get_md5.file_get_md5(file_md5_path)
        if local_md5 == file_md5:
            send_code = {'code': 200}
            logging.info('Check %s FIles, Success!')
            self.send_messages(send_code)
            return True
        else:
            send_code = {'code': 199}
            logging.error('Check %s Files, Failure!')
            self.send_messages(send_code)


    def login(self,response):
        '''
        客户端发送请求，服务端执行登陆功能
        :param response: 信息字典
        :return:
        '''
        user,pwd = response['user'],response['pwd']
        pwd = Get_md5.get_md5(user,pwd) # MD5加密加盐
        iter_user = FileReadWrite.file_read(settings.userinfo) # 用户信息文件生成器
        for iter_u in iter_user:
            if user == iter_u['user'] and pwd == iter_u['pwd']:
                send_code = {'code': 203}
                self.name = iter_u['user'] # 修改self.name 为登陆成功用户
                self.path = os.path.join(settings.home,self.name)  # 修改为用户默认家目录
                logging.info('%s Login Success，Swithed to the user home dir ...'%user)
                self.send_messages(send_code)  # 发送执行结果
                break
        else:
            send_code = {'code':204}
            self.send_messages(send_code)


    def register(self,response):
        '''
        用户注册
        :param response:  用户信息指令字典
        :return:
        '''
        user,pwd = response['register_user'],response['register_pwd']
        pwd = Get_md5.get_md5(user,pwd) # MD5加密码撒盐
        user_info = {'user':user,'pwd':pwd}
        iter_con = FileReadWrite.file_read(settings.userinfo)
        for iter_u in iter_con:  # 循环遍历生成器
            if user == iter_u['user']: # 判断登陆用户是否已存在
                send_code = {'code':202}
                self.send_messages(send_code)
                break
        else:
            FileReadWrite.file_write(settings.userinfo,user_info)
            os.mkdir(os.path.join(settings.home,user))
            ret = {'code':201}
            logging.info('Create User: %s Success ! '%user)
            self.send_messages(ret)

    def upload(self, cmd_dict):
        '''
         客户端文件上传
        :param cmd_dict: 信息字典
        :param conn: 发现和接受消息的对象
        :return:
        '''
        file_md5 = cmd_dict['file_md5']
        fine_name = cmd_dict['file_name']
        file_md5_path = os.path.join(self.path, file_md5)
        file_name_path = os.path.join(self.path, fine_name)
        upload_size = cmd_dict['file_size']

        # 判断MD5文件是否存在，存在表示有断点，否则表示从0开始
        if not os.path.exists(file_md5_path):
            response = {'code': 101}  # 存在表示有断点
            self.send_messages(response)  # 发送信息
            self.recv_file(file_md5_path, 0, upload_size) # 开始接收写入文件
            logging.info('User %s ,Start Upload, Upload from 0 !'%self.name)

        else: # 断点续传
            exist_size = os.path.getsize(file_md5_path)
            response = {'code': 102, 'exist_size': exist_size}
            self.send_messages(response)
            self.recv_file(file_md5_path, exist_size, upload_size)
            logging.info('User %s , Start Breakpoint Upload，Upload from %s'%(self.name,exist_size))

        # 合法性校验
        ret = self.__md5_check(file_md5, file_md5_path)
        # 文件重命名
        if ret: self.__file_rename(file_name_path, file_md5_path)

    def download(self,response):
        '''
        客户端下载
        :param response: 客户端请求信息
        '''
        file_name = response['file_name'] # 文件名称
        file_path = os.path.join(self.path,file_name) # 拼接本地文件路径
        if os.path.exists(file_path):  # 文件存在
            file_size = os.path.getsize(file_path)  # 计算大小
            file_md5 = Get_md5.file_get_md5(file_path) # 获取MD5值

            file_info_dic = {'file_size':file_size,'file_md5':file_md5} # 发送头信息
            self.send_messages(file_info_dic)  # 发送头信息
            recv_code = self.recv_messages()  # 接收返回值

            if recv_code['code'] == 103:  # 从0开始
                logging.info('User %s ,Start Download, Download from 0 !' % self.name)
                self.send_file(file_path,0,file_size)

            elif recv_code['code'] == 104:  # 断点开始下载
                exist_size = recv_code['exist_size']
                logging.info('User %s ,Start Download, Download from %s !' %(self.name,exist_size))
                self.send_file(file_path,exist_size,file_size)


    def showFileDir(self,response=None):
        '''
        查看当前目录下文件夹或文件
        :param response:
        :return:
        '''
        cont = os.listdir(self.path)  # 当前目录下内容列表
        cont_dict = {'content_lit': cont}
        logging.info('User %s , Show dir content !' % (self.name))
        self.send_messages(cont_dict) # 发送信息

    def create_dir(self,cmd_dict):
        '''
        当前目录下创建子目录
        :param cmd_dict:  # 客户端请求信息字典
        :return:
        '''
        dir_name = cmd_dict['dir_name']  # 创建的目录名称
        new_path = os.path.join(self.path,dir_name)
        if not os.path.exists(new_path): # 判断目录是否已存在
            os.mkdir(new_path)  # 不存在创建
            logging.info('User %s , Create %s dir !' % (self.name,new_path))
            send_code = {'code':205}
            self.send_messages(send_code)
        else:
            logging.warning('User %s , %s dir existed !' % (self.name,new_path))
            send_code = {'code':206}
            self.send_messages(send_code)

    def cdNextDir(self,cmd_dict):
        '''
        进入下一级目录
        '''
        cd_path = os.path.join(self.path,cmd_dict['dirname'])  # 拼接绝对路径
        if os.path.isdir(cd_path): # 判断是目录
            self.path = cd_path  # 当前目录修改为拼接以后的目录
            logging.info('User %s ,cd new dir : %s !' % (self.name, self.path))
            send_code = {'code':207}
            self.send_messages(send_code)
        else:
            send_code = {'code': 208}
            self.send_messages(send_code)

    def cdUpperDir(self,response=None):
        '''返回上一级目录'''
        cc = os.path.dirname(self.path) # 取上一级目录名称
        self.path = cc  # 重新赋值
        logging.info('User %s ,return on  dir : %s !' % (self.name, self.path))
        send_code = {'code':209}
        self.send_messages(send_code)