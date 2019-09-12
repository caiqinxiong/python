# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:24
import socketserver
import json
import os
from conf import settings as ss
from core.log import Log as log
from core.server_common import Common as cn
from core.server_auth import ServerAuth as sa

class FtpServer(socketserver.BaseRequestHandler):

    def setup(self):
        self.pwd_path = ss.DB_PATH
        os.chdir(self.pwd_path)

    def login(self,opt_dict):
        '''登录'''
        return cn.mySend(self.request,sa.auth(opt_dict))

    def register(self,opt_dict):
        '''注册'''
        return cn.mySend(self.request,sa.auth(opt_dict))

    def userHome(self,opt_dict):
        '''用户家目录'''
        self.user_home = ss.USER_HOME(opt_dict['name'])
        if not os.path.exists(self.pwd_path):os.makedirs(self.user_home)
        os.chdir(self.user_home)

    def viewDir(self,opt_dict):
        '''查看当前目录'''
        opt_dict['msg'] = '服务器的%s目录信息如下：' % self.pwd_path
        for index,name in enumerate(os.listdir(self.pwd_path),1):
            path = os.path.join(self.pwd_path,name)
            if os.path.isfile(path):
               opt_dict['msg'] += '\n文件%s：%s' % (index, name)
            elif os.path.isdir(path):
                opt_dict['msg'] += '\n目录%s：%s' % (index, name)
        return cn.mySend(self.request,opt_dict,True)

    def mkdir(self,opt_dict):
        '''创建目录'''
        if os.path.exists(os.path.abspath(opt_dict['dirname'])):
            opt_dict['msg'] = '%s目录已存在！' % opt_dict['dirname']
        else:
            os.mkdir(opt_dict['dirname'])
            opt_dict['msg'] = '%s目录创建成功！' % os.path.abspath(opt_dict['dirname'])
        return cn.mySend(self.request,opt_dict,True)

    def rmdir(self,opt_dict):
        '''删除空目录'''
        try:
            os.rmdir(os.path.abspath(opt_dict['dirname']))
            opt_dict['msg'] = '%s目录删除成功！' % opt_dict['dirname']
        except OSError as e:
            opt_dict['msg'] = '目录不存在或目录不为空！\n%s' % e
        return cn.mySend(self.request,opt_dict,True)

    def rmfile(self,opt_dict):
        '''删除文件'''
        name = os.path.abspath(opt_dict['filename'])
        if os.path.isfile(name):
            os.remove(name)
            opt_dict['msg'] = '%s文件删除成功！' % name
        else:
            opt_dict['msg'] = '%s文件不存在！' % name
        return cn.mySend(self.request,opt_dict,True)

    def changeDir(self,opt_dict):
        '''切换子目录'''
        name = os.path.abspath(opt_dict['dirname'])
        if os.path.isdir(name):
            os.chdir(name)
            self.pwd_path = name
            opt_dict['msg'] = '已切换到%s' % name
        else:
            opt_dict['msg'] = '%s目录不存在！' % name
        return cn.mySend(self.request,opt_dict,True)

    def getFile(self,opt_dict):
        '''客户端从服务器下载文件'''
        if not os.path.exists(opt_dict['file_path']): #判断服务器上是否存在该文件
            opt_dict['flag'] = False
            opt_dict['msg'] = '%s文件不存在！' % opt_dict['file_path']
            log.readAndWrite(opt_dict['msg'])
        else:
            opt_dict['flag'] = True # 文件存在
            opt_dict['total_size'] = os.path.getsize(opt_dict['file_path']) # 获取文件总字节大小
            opt_dict['filesize'] = opt_dict['total_size'] - opt_dict['exist_size'] # 如果文件存在，获取要传输的文件剩余大小
        dic_b = json.dumps(opt_dict).encode('utf-8')
        cn.mySend(self.request,dic_b) # 将文件基本信息反馈给客户端
        if opt_dict['flag']:cn.startGetFile(self.request,opt_dict) # 文件存在，开始发送文件给客户端

    def putFile(self,opt_dict):
        '''客户端上传文件到服务器'''
        opt_dict['total_size'] = os.path.getsize(opt_dict['file_path']) # 获取文件大小
        put_path = ss.UPLOAD(opt_dict['name'])
        if not os.path.exists(put_path):os.makedirs(put_path)
        opt_dict['upload_file'] = os.path.join(put_path,os.path.basename(opt_dict['file_path']))
        opt_dict['exist_size'] =  os.path.getsize(opt_dict['upload_file']) if os.path.exists(opt_dict['upload_file']) else 0 # 判断上传文件服务器上是否存在，做断点续传
        opt_dict['filesize'] = opt_dict['total_size'] - opt_dict['exist_size'] # 如果文件存在，获取要传输的文件剩余大小
        opt_dict = cn.checkQuota(ss.USER_FILE,opt_dict) # 校验用户在服务器的磁盘配额
        log.readAndWrite(opt_dict['msg'])
        dic_b = json.dumps(opt_dict).encode('utf-8')
        cn.mySend(self.request,dic_b) # 将文件基本信息反馈给客户端
        if opt_dict['flag']:cn.startPutFile(self.request,opt_dict) # 开始接收客户端上传的文件

    def handle(self):
        '''方法重写，重写handle函数，启动socketserver时执行该函数，看一下socketserver源码'''
        while True:
            try:
                log.readAndWrite("客户端%s已链接！" % (self.client_address[0]))
                log.debug('等待客户端发送操作命令...')
                dic_str = cn.myRecv(self.request).decode('utf-8')# 接收客户端发送指令
                if not dic_str.find('exit') < 0:
                    log.readAndWrite("客户端%s已主动断开链接！" % (self.client_address[0]))
                    break
                elif not dic_str.find('error') < 0:
                    log.warning('客户端操作错误！')# 客户端报错时，服务器不进行任何操作！
                else:
                    opt_dict = json.loads(dic_str)
                    if hasattr(self,opt_dict['operate']):getattr(self,opt_dict['operate'])(opt_dict)
            except ConnectionResetError as e:
                log.error("%s客户端已断开%s"%(self.client_address,e))
                break

def runServer():
    '''启动FTP服务器'''
    server = socketserver.ThreadingTCPServer(ss.IP_PORT,FtpServer)
    server.serve_forever()
