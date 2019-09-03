# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:24
import sys,os,socket,hashlib,socketserver,json,time
import struct
from conf import settings as ss
from core.log import Log as log
from core.common import Common as cn
class FtpServer(socketserver.BaseRequestHandler):

    # def mySend(self,msg):
    #     msgb = msg.encode('utf-8')
    #     len_msg = len(msgb)
    #     pack_len = struct.pack('i', len_msg)
    #     self.request.send(pack_len)
    #     self.request.send(msgb)
    #
    # def myRecv(self):
    #     '''解决粘包'''
    #     pack_len = self.request.recv(4)
    #     len_msg = struct.unpack('i', pack_len)[0]
    #     msg = self.request.recv(len_msg).decode('utf-8')
    #     return msg

    def getFile(self):
        '''接收客户端上传的文件'''
        cn.getFile(self.request)
        # file_dic = self.request.recv(1024).decode('utf-8')
        # file_dic = self.myRecv()
        # file_dic = cn.myRecv(self.request)
        # dic = json.loads(file_dic)
        # with open(dic['filename'],mode='w',encoding='utf-8') as f:
        #     while dic['filesize']>0:
        #         # file_content = self.request.recv(1024)
        #         # file_content = self.myRecv()
        #         file_content = cn.myRecv(self.request)
        #         dic['filesize'] -= len(file_content)
        #         f.write(file_content)

    def putFile(self,file_path,name):
        '''从服务器下载文件到客户端'''
        cn.putFile(self.request,file_path,name)
        # 输入需要发送的文件,获取并发送文件大小
        # put_path = ss.USER_CLIENT(name)
        # if not os.path.exists(put_path):os.makedirs(put_path)
        # file_name = os.path.join(put_path,os.path.basename(file_path))
        # file_size = os.path.getsize(file_path)
        # dic = {'filename':file_name,'filesize':file_size}
        # str_dic = json.dumps(dic)
        # # dic_b = str_dic.encode('utf-8')
        # # self.request.send(dic_b)
        # # self.mySend(str_dic)
        # cn.mySend(self.request,str_dic)
        # with open(file_path,mode = 'r',encoding='utf-8') as f:
        #     # content = f.read()
        #     # self.mySend(content)
        #     for line in f:
        #         # if line.strip():self.mySend(line)
        #         if line.strip():cn.mySend(self.request,line)
        #     # self.request.send(content)
        # self.request.close()

    def handle(self):
        '''方法重写，重写handle函数，启动socketserver时执行该函数，看一下socketserver源码'''
        while True:
            try:
                # conn = self.request
                self.getFile()
                # file_path = r'E:\python_test\python\day09\homework\FTP\db\users_home\caiqinxiong\server_home\2019-09-02-log'
                # self.putFile(file_path,'caiqinxiong')
                break
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

server = socketserver.ThreadingTCPServer(ss.IP_PORT,FtpServer)
server.serve_forever()

