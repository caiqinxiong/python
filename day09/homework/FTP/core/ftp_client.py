# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:23
import sys,os,socket,hashlib,time,json
from conf import settings as ss
from core import user
class FtpClient:
    '''FTP客户端类'''
    def __init__(self):
        pass

    def putFile(self,file_path):
        '''上传文件'''
        sk = socket.socket()
        sk.connect(ss.IP_PORT)
        # 输入需要发送的文件,获取并发送文件大小
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        dic = {'filename':file_name,'filesize':file_size}
        str_dic = json.dumps(dic)
        dic_b = str_dic.encode('utf-8')
        sk.send(dic_b)
        with open(file_path,mode = 'rb') as f:
            content = f.read()
            sk.send(content)
        sk.close()

f = FtpClient()
f.putFile(r'E:\python_test\python\day09\homework\FTP\log\2019-09-02-log')