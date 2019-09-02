# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:24
import sys,os,socket,hashlib,socketserver,json,time
from conf import settings as ss
from core.log import Log as log
class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        '''方法重写，重写handle函数，启动socketserver时执行该函数，看一下socketserver源码'''
        while True:
            try:
                conn = self.request
                file_dic = conn.recv(1024).decode('utf-8')
                dic = json.loads(file_dic)
                self.getFile(conn,dic)
                # self.data = self.request.recv(1024).decode('utf-8')
                # log.readAndWrite("%s已链接" % (self.client_address))
                # opt_dict = json.loads(self.data)
                # print('in the handle',opt_dict["action"])
                # if hasattr(self,str(opt_dict["action"])):
                #     func = getattr(self,str(opt_dict["action"]))
                #     func(opt_dict)
            except ConnectionResetError as e:
                log.readAndWrite("%s客户端已断开%s"%(self.client_address,e))
                break

    def getFile(self,conn,dic):
        '''下载文件'''
        with open(dic['filename'],mode='wb') as f:
            while dic['filesize']>0:
                file_content = conn.recv(1024)
                dic['filesize'] -= len(file_content)
                f.write(file_content)

server = socketserver.ThreadingTCPServer(ss.IP_PORT,FtpServer)
server.serve_forever()
