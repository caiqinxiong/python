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
        msg_b = conn.recv(len_msg)
        return msg_b

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
    def startGetFile(cls,conn,dic):
        '''接收文件，客户端从服务器下载文件'''
        md5 = hashlib.md5() # 接收数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        total = dic['total_size']
        num = dic['exist_size']
        if dic['exist_size']:log.debug('文件上次已经下载了%s字节，开始断点下载！' % dic['exist_size'])
        with open(dic['download_file'],mode='ab') as f:
            while dic['filesize']>0:
                # file_content = cls.myRecv(conn)
                file_content = conn.recv(1024*1000)
                dic['filesize'] -= len(file_content) # 剩余接收文件大小
                f.write(file_content)
                num += len(file_content) # 累计发送文件大小
                cls.processBar(num,total) # 进度条
                md5.update(file_content)
        clinet_md5 = md5.hexdigest() # 自己的MD5值
        cls.mySend(conn,clinet_md5.encode())# 发送MD5值给服务器做校验
        dic_str = cls.myRecv(conn).decode() # 接收校验结果，返回字典
        opt_dic = json.loads(dic_str)
        log.readAndWrite(opt_dic['msg'])
        return opt_dic

    @classmethod
    def startPutFile(cls,conn,dic):
        '''发送文件，从客户端发送文件到服务器'''
        md5 = hashlib.md5() # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        total = dic['filesize']
        num = dic['exist_size']
        if dic['exist_size']:log.debug('文件上次已经上传了%s字节，开始断点上传！' % dic['exist_size'])
        with open(dic['file_path'],mode = 'rb') as f:
            f.seek(dic['exist_size']) # 将指针移动到指定位置开始读
            # for line in f:
            # # if line.strip():不能添加判断，要不导致发送的数据不全，文件内容不管是什么都给发送过去就行
            #     cls.mySend(conn,line)
            while total>0:
                line = f.read(1024*1000)
                conn.send(line)# 发生粘包也没有关系，反正最后把文件传完就行
                num += len(line) # 累计发送文件大小，传输进度条用
                total -= len(line) # 退出循环用
                cls.processBar(num,dic['total_size'])
                md5.update(line)
        clinet_md5 = md5.hexdigest() # 自己发送数据的MD5值
        cls.mySend(conn,clinet_md5.encode())# 发送MD5值给服务器做校验
        dic_str = cls.myRecv(conn).decode() # 接收校验结果，返回字典
        opt_dic = json.loads(dic_str)
        log.readAndWrite(opt_dic['msg'])
        return opt_dic


