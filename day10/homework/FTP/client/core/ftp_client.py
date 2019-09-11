# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:23
import socket
import os
import time
import json
from conf import settings as ss
from core.log import Log as log
from core.client_common import Common as cn
from core.client_auth import ClinetAuth

class FtpClient:
    '''FTP客户端类'''
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(ss.IP_PORT)
        # self.pwd_path = ss.USER_HOME(self.name)
        # if not os.path.exists(self.pwd_path):os.makedirs(self.pwd_path)
        # os.chdir(self.pwd_path)

    def putFile(self):
        '''客户端上传文件到服务器'''
        file_path = input('请输入要上传到服务器的文件路径：').strip()
        if not os.path.isfile(file_path):# 客户端上传文件，自己先判断文件是否存在
            cn.mySend(self.sk,b'error')
            return log.error('%s文件不存在!' % file_path)
        opt_dict = {'operate':'putFile', 'file_path':file_path, 'name':self.name}
        dic_b = json.dumps(opt_dict).encode('utf-8')
        cn.mySend(self.sk,dic_b) # 将执行命令发送给服务器，服务执行相应函数
        dic_str = cn.myRecv(self.sk).decode('utf-8') # 接收服务器回应信息
        opt_dict = json.loads(dic_str)
        log.debug(opt_dict['msg'])
        if opt_dict['flag']:# 该用户在服务器的磁盘配额满足
            log.debug('开始上传%s到服务器！' % opt_dict['file_path'])
            cn.startPutFile(self.sk,opt_dict)


    def getFile(self):
        '''客户端从服务器下载文件'''
        file_path = input('请输入要从服务器下载的文件路径：').strip()
        download_path = ss.DOWNLOAD(self.name) # 指定下载目录
        if not os.path.exists(download_path):os.makedirs(download_path)
        download_file = os.path.join(download_path,os.path.basename(file_path)) # 下载到客户端本地的文件路径
        exist_size =  os.path.getsize(download_file) if os.path.exists(download_file) else 0 # 判断本地文件是否存在，做断点续传
        opt_dict = {'operate':'getFile', 'file_path':file_path, 'download_file':download_file, 'exist_size':exist_size, 'name':self.name}
        dic_b = json.dumps(opt_dict).encode('utf-8')
        cn.mySend(self.sk,dic_b) # 将执行命令发送给服务器，服务执行相应函数
        dic_str = cn.myRecv(self.sk).decode('utf-8') # 接收服务器回应信息
        opt_dict = json.loads(dic_str)
        if opt_dict['flag']: # 文件存在
            log.debug('开始服务器中下载文件%s' % opt_dict['file_path'] )
            cn.startGetFile(self.sk,opt_dict)
        else:
            log.debug(opt_dict['msg'])



    def viewDir(self):
        '''查看当前目录'''
        log.debug('%s目录信息如下：' % self.pwd_path)
        for index,name in enumerate(os.listdir(self.pwd_path),1):
            path = os.path.join(self.pwd_path,name)
            if os.path.isfile(path):
               log.debug('文件%s：%s' % (index, name))
            elif os.path.isdir(path):
                log.debug('目录%s：%s' % (index, name))

    def mkdir(self):
        '''创建目录'''
        name = input('请输入新建文件夹名称：')
        if os.path.exists(os.path.abspath(name)):
            log.warning('%s目录已存在！' % name)
        else:
            os.mkdir(name)
            log.readAndWrite('%s目录创建成功！' % os.path.abspath(name))

    def rmdir(self):
        '''删除空目录'''
        name = input('请输入要删除的空文件夹名称：')
        try:
            os.rmdir(os.path.abspath(name))
            log.readAndWrite('%s目录删除成功！' % name)
        except OSError as e:
            log.warning('目录不存在或目录不为空！\n%s' % e)

    def rmfile(self):
        '''删除文件'''
        name = input('请输入要删除的文件名称：')
        name = os.path.abspath(name)
        if os.path.isfile(name):
            os.remove(name)
            log.readAndWrite('%s文件删除成功！' % name)
        else:
            log.warning('%s文件不存在！' % name)

    def changeDir(self):
        '''切换子目录'''
        name = input('请输入切换目录名称：')
        name = os.path.abspath(name)
        if os.path.isdir(name):
            os.chdir(name)
            self.pwd_path = name
            log.debug('已切换到%s' % name)
        else:
            log.warning('%s目录不存在！' % name)

    def quit(self):
        log.debug('谢谢使用！')
        cn.mySend(self.sk,b'exit')
        self.sk.close()
        exit(-1)

    def clientView(self):
        '''客户端视图'''
        head = '*' * 20 + '\n欢迎使用FTP服务器！\n' + '*' * 20
        opt_list = [('上传文件','putFile'),('下载文件','getFile'),('查看当前目录信息','viewDir'),('创建目录','mkdir'),
                    ('删除空目录','rmdir'),('删除文件','rmfile'),('切换子目录','changeDir'),('退出','quit')]
        while True:
            print('\033[35;1m%s\033[0m' % head)
            for index,opt in enumerate(opt_list,1):print('\033[35;1m%s、%s\033[0m' % (index, opt[0])) # 打印操作列表信息
            try:
                num = int(input( '请输入您要选择的操作序号:'))
                if hasattr(self,opt_list[num-1][1]):getattr(self,opt_list[num-1][1])() # 反射
            except ValueError as e:
                log.error('%s不是效数字！！' % e)
            except IndexError as e:
                log.error('%s\n请输入1-12的有效数字！！' % e)
            print('3秒后自动跳转回主页面！')
            time.sleep(3)

    def run(self):
        '''身份认证'''
        opt_dict = ClinetAuth(self.sk).main()
        if opt_dict['flag']:
            self.name = opt_dict['name']
            self.clientView()
        else:
            self.quit()
