# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/3 14:35
import struct
import json
import os
import sys
import hashlib
from conf import settings as ss
from core.log import Log as log

class Common:
    '''公共类'''
    def __init__(self):
        pass

    @staticmethod
    def mySend(conn,msgb):
        '''发送数据时，解决粘包问题'''
        len_msg = len(msgb)
        pack_len = struct.pack('i', len_msg)
        conn.send(pack_len)
        conn.send(msgb)

    @staticmethod
    def myRecv(conn):
        '''接收数据时，解决粘包问题'''
        pack_len = conn.recv(4) #struct机制，在发送数据前，加上固定长度4字节的头部
        len_msg = struct.unpack('i', pack_len)[0] # 解包，得到元组。
        msg = conn.recv(len_msg)
        return msg

    @staticmethod
    def processBar(num, total):
        '''打印进度条'''
        rate = num / total
        rate_num = int(rate * 100)
        bar = ('>' * rate_num, rate_num,) # 展示的进度条符号
        r = '\r%s>%d%%\n' % bar if rate_num == 100 else '\r%s>%d%%' % bar
        sys.stdout.write(r) # 覆盖写入
        return  sys.stdout.flush # 实时刷新

    @classmethod
    def getFile(cls,conn):
        '''接收文件'''
        file_dic = cls.myRecv(conn) # 接收数据，解决粘包函数
        dic = json.loads(file_dic.decode()) # 将接收到的二进制先转换成字符串，再loads还原字典
        md5 = hashlib.md5() # 接收数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        total = dic['filesize']
        num = 0
        with open(dic['filename'],mode='wb') as f:
            while dic['filesize']>0:
                file_content = cls.myRecv(conn)
                dic['filesize'] -= len(file_content) # 剩余接收文件大小
                f.write(file_content)
                num += len(file_content) # 累计发送文件大小
                cls.processBar(num,total) # 进度条
                md5.update(file_content)
        ret = md5.hexdigest() # 自己的MD5值
        cls.mySend(conn,ret.encode())# 发送MD5值给对方做校验
        ret_r = cls.myRecv(conn).decode() # 接收对方的MD5值
        check = 'MD5校验OK，文件传输成功！' if ret == ret_r else 'MD5不一致，文件传输失败！'
        conn.close()
        return (ret,dic['filename'],check)


    @classmethod
    def putFile(cls,conn,file,put_path,name):
        '''发送文件'''
        # 输入需要发送的文件,获取并发送文件大小
        put_path = put_path(name) # 文件存储路径
        if not os.path.exists(put_path):os.makedirs(put_path)
        file_name = os.path.join(put_path,os.path.basename(file))
        file_size = os.path.getsize(file) # 获取文件总字节大小
        dic = {'filename':file_name,'filesize':file_size}
        dic_b = json.dumps(dic).encode() # 将字典dumps成字符串，再转换成byte。网络传输只能传输byte哦。
        cls.mySend(conn,dic_b)# 发送数据，解决粘包函数
        md5 = hashlib.md5() # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        num = 0
        with open(file,mode = 'rb') as f:
            for line in f:
            # if line.strip():不能添加判断，要不导致发送的数据不全，文件内容不管是什么都给发送过去就行
                cls.mySend(conn,line)
                num += len(line) # 累计发送文件大小
                cls.processBar(num,file_size)
                md5.update(line)
        ret = md5.hexdigest() # 自己发送数据的MD5值
        cls.mySend(conn,ret.encode())# 发送MD5值给对方做校验
        ret_r = cls.myRecv(conn).decode() # 接收对方的MD5值
        check = 'MD5校验OK，文件传输成功！' if ret == ret_r else 'MD5不一致，文件传输失败！'
        conn.close()
        return (ret,file_name,check)


