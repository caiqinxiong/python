#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/4'

import os
from conf import settings
from core.combination import Combination
from core.warpper import format_wrapper

class Program(Combination):
    '''客户端主要功能'''
    # 功能列表，用于反射
    program_list = [
        ('文件上传','upload'),
        ('文件下载','download'),
        ('查看目录或文件','showFileDir'),
        ('创建目录','create_dir'),
        ('进入下一级目录','cdNextDir'),
        ('进入上一级目录','cdUpperDir'),
        ('退出','quit')
    ]

    def __init__(self,sk):
        self.conn = sk

    def __file_rename(self,file_name_path,file_md5_path):
        '''
        # 封装一个内部使用的重命名函数
        :param file_name_path: 文件名称绝对路径
        :param file_md5_path:  文件MD5绝对路径
        :return:
        '''

        # 判断文件不存在
        if  not os.path.exists(file_name_path):
            # MD5文件路径重命名
            os.rename(file_md5_path, file_name_path)
        else:
            num = 1
            while True: # 死循环
                file_name = os.path.basename(file_name_path) # 文件名称
                file_path = os.path.dirname(file_name_path)  # 文件夹路径
                file,geshi = file_name.rsplit('.',maxsplit=1) # 文件名称从结尾切割,最多切割1次
                new_name = '{0}_copy{1}.{2}'.format(file,num,geshi) # 新的名称
                new_path = os.path.join(file_path,new_name)  # 路径拼接
                if not os.path.exists(new_path):   # 判断新文件不存在
                    os.rename(file_md5_path, new_path) # 重命名
                    break  # 结束循环
                else:
                    num+=1
                    continue # 数字重新赋值，跳出本层循环

    def __md5_check(self,file_md5,file_md5_path):
        '''
        封装一个内部使用的MD5校验(文件下载功能)
        :param file_md5: 服务端发送过来的完整文件MD5值
        :param file_md5_path:  当前文件
        '''
        local_md5 = self.file_get_md5(file_md5_path) # 调用计算文件MD5函数，计算传参进来文件的MD5值
        if local_md5 == file_md5: # 判断 MD5值是否一样
            print(settings.code[198])
            return True
        else:
            print(settings.code[197])

    @format_wrapper
    def upload(self):
        '''文件上传 '''
        file_path = input('文件路径：').strip()
        if os.path.exists(file_path):  # 判断路径文件是否在
            file_name = os.path.basename(file_path)  # 文件名称
            file_size = os.path.getsize(file_path)   # 文件大小
            file_md5 = self.file_get_md5(file_path)  # 文件md5值

            # 信息字典
            info_dict = {'cmd': 'upload', 'file_name': file_name, 'file_size': file_size, 'file_md5': file_md5}
            # 发送
            self.send_messages(info_dict)
            # 接受返回值
            response = self.recv_messages()

            if response['code'] == 101: # 从头开始上传
                print(settings.code[101])
                self.send_file(file_path,0, file_size) # 发送文件
                recv_code = self.recv_messages() # 接受返回值信息
                print(settings.code[recv_code['code']])

            elif response['code'] == 102: # 断电续传
                print(settings.code[102])
                exist_size = response['exist_size'] # 返回的已上传文件字节数
                self.send_file(file_path,exist_size, file_size) # 将文件字节数作为重新续传的起始点
                recv_code = self.recv_messages()  # 接受返回值
                print(settings.code[recv_code['code']])

    @format_wrapper
    def download(self):
        '''文件下载'''
        dir_list = self.showFileDir() # 列出服务端当前目录下内容
        down_input = int(input('请输入当前目录下要下载的内容: ').strip()) # 序号选择
        write_path = input('请输入要保存的位置: ').strip() # 保存的本地路径

        if os.path.exists(write_path): # 判断文件路径存在
            file_path = {'cmd': 'download', 'file_name': dir_list[down_input - 1]} # 生成指令字典
            self.send_messages(file_path)  # 发送消息

            response = self.recv_messages() # 接受返回值
            file_md5_path = os.path.join(write_path, response['file_md5']) # 文件MD5的路径
            file_name_path = os.path.join(write_path, file_path['file_name']) # 文件的名称
            download_size = response['file_size']  # 下载的文件大小

            if not os.path.exists(file_md5_path): # 判断文件不存在
                send_code = {'code':103}
                self.send_messages(send_code)
                print('开始下载')
                self.recv_file(file_md5_path,0,download_size) # 从头开始下载

            else: # 断点续传
                exist_size = os.path.getsize(file_md5_path) # 获取本地已下载的文件总大小
                send_code = {'code': 104,'exist_size': exist_size}
                self.send_messages(send_code)  # 发送信息
                print('从断点开始下载')
                self.recv_file(file_md5_path,exist_size,download_size) # 接文件已接收大小作文续传起点

            # md5文件校验
            ret = self.__md5_check(response['file_md5'], file_md5_path)
            # 文件重命名
            if ret: self.__file_rename(file_name_path, file_md5_path)

        else:
            print('本地的路径不存在')


    def showFileDir(self):
        '''查看当前目录下文件或目录'''
        cmd_dict = {'cmd':'showFileDir'}
        self.send_messages(cmd_dict) # 发送指令
        # 接受返回值
        response = self.recv_messages()
        # 循环打印列表
        print('**'*3,self.showFileDir.__doc__,'**'*3)
        for index,file in enumerate(response['content_lit'],1):
            print(index,file)
        print('**'*17)
        # 返回当前目录列表
        return response['content_lit']

    @format_wrapper
    def create_dir(self):
        '''目录创建'''
        dir_name = input('创建目录名：').strip()
        cmd_dict = {'cmd': 'create_dir','dir_name': dir_name}
        self.send_messages(cmd_dict) # 发送指令及文件名称信息

        # 接受返回值
        recv_code = self.recv_messages()
        if recv_code['code'] == 205:
            # 205表示创建成功
            print(settings.code[205])
            return
        else:
            # 206创建失败
            print(settings.code[206])
            print('请重新创建')
            # 递归直接该函数
            self.create_dir()

    @format_wrapper
    def cdNextDir(self):
        '''进入下一级目录'''
        path = self.showFileDir() # 打印当前目录下内容
        dir_name = int(input('切换下一层目录,请输入序号：').strip())
        cmd_dict = {'cmd':'cdNextDir','dirname':path[dir_name-1]}
        self.send_messages(cmd_dict) # 发送指令
        recv_code = self.recv_messages()  # 接受返回值
        print(settings.code[recv_code['code']]) # 打印结果

    @format_wrapper
    def cdUpperDir(self):
        '''返回上一级目录'''
        cmd_dict = {'cmd': 'cdUpperDir'}
        self.send_messages(cmd_dict) # 发送指令
        recv_code = self.recv_messages() # 接受返回值
        print(settings.code[recv_code['code']])
