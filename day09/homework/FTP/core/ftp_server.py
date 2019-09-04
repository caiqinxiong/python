# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:24
import socketserver
import json
from conf import settings as ss
from core.log import Log as log
from core.common import Common as cn
class FtpServer(socketserver.BaseRequestHandler):

    def getFile(self,opt_dict):
        '''接收客户端上传的文件'''
        ret = cn.getFile(self.request)
        log.debug(ret[1]+'\n'+ret[2]+'\nMD5值：\n'+ret[0])

    def putFile(self,opt_dict):
        '''从服务器下载文件到客户端'''
        ret = cn.putFile(self.request,opt_dict['file_path'],ss.USER_CLIENT,opt_dict['name'])
        log.debug(ret[1]+'\n'+ret[2]+'\nMD5值：\n'+ret[0])


    def handle(self):
        '''方法重写，重写handle函数，启动socketserver时执行该函数，看一下socketserver源码'''
        while True:
            try:
                log.readAndWrite("客户端%s已链接！" % (self.client_address[0]))
                log.debug('等待客户端发送操作命令...')
                dic_str = cn.myRecv(self.request).decode()# 接收客户端发送指令
                if not dic_str.find('exit') < 0:
                    log.readAndWrite("客户端%s已主动断开链接！" % (self.client_address[0]))
                    break
                elif not dic_str.find('error') < 0:
                    log.warning('客户端操作错误！')# 客户端报错时，服务器不进行任何操作！
                else:
                    opt_dict = json.loads(dic_str)
                    if hasattr(self,opt_dict['action']):getattr(self,opt_dict['action'])(opt_dict)
            except ConnectionResetError as e:
                log.error("%s客户端已断开%s"%(self.client_address,e))
                break

def runServer():
    '''启动FTP服务器'''
    server = socketserver.ThreadingTCPServer(ss.IP_PORT,FtpServer)
    server.serve_forever()

