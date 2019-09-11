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

    def login(self,opt_dict):
        '''登录'''
        return cn.mySend(self.request,sa.auth(opt_dict))

    def register(self,opt_dict):
        '''注册'''
        return cn.mySend(self.request,sa.auth(opt_dict))

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
