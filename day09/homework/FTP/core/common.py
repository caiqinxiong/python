# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/3 14:35
import struct
import json
import os
import hashlib
from conf import settings as ss

class Common:
    '''公共类'''
    def __init__(self):
        pass

    @staticmethod
    def getFileMD5(file):
       '''对文件做MD5校验'''
       md5 = hashlib.md5()
       with open(file,'rb') as f:
           for line in f:
               if line.strip():md5.update(line)
       return md5.hexdigest()

    @staticmethod
    def mySend(conn,msg):
        '''发送数据时，解决粘包问题'''
        msgb = msg
        len_msg = len(msgb)
        pack_len = struct.pack('i', len_msg)
        conn.send(pack_len)
        conn.send(msgb)

    @staticmethod
    def myRecv(conn):
        '''接收数据时，解决粘包问题'''
        try:
            pack_len = conn.recv(4)
            len_msg = struct.unpack('i', pack_len)[0]
            msg = conn.recv(len_msg)
        except:
            msg = conn.recv(1024*2)
        return msg

    @staticmethod
    def getFile(conn):
        '''接收文件'''
        file_dic = Common.myRecv(conn)
        dic = json.loads(file_dic.decode())
        with open(dic['filename'],mode='wb') as f:
            while dic['filesize']>0:
                print(dic['filesize'])
                file_content = Common.myRecv(conn)
                print(file_content)
                dic['filesize'] -= len(file_content)
                f.write(file_content)
                if not file_content:break
        conn.close()

    @staticmethod
    def putFile(conn,file_path,name):
        '''发送文件'''
        # 输入需要发送的文件,获取并发送文件大小
        put_path = ss.USER_CLIENT(name)
        if not os.path.exists(put_path):os.makedirs(put_path)
        file_name = os.path.join(put_path,os.path.basename(file_path))
        file_size = os.path.getsize(file_path)
        dic = {'filename':file_name,'filesize':file_size}
        str_dic = json.dumps(dic)
        dic_b = str_dic.encode()
        Common.mySend(conn,dic_b)
        with open(file_path,mode = 'rb') as f:
            for line in f:
                if line.strip():Common.mySend(conn,line)
        conn.close()
