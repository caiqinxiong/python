# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/3 14:35
import struct
import json
import os
import sys
import hashlib
from core.server_auth import ServerAuth as sa
from core.log import Log as log
from conf import settings as ss

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

    @staticmethod
    def updateQuota(file,name,quota_new):
        '''更新磁盘配额'''
        with open(file,mode='r',encoding='utf-8') as f1,open(file + '.bak',mode='w',encoding='utf-8') as f2:
            for line in f1:
                if line.strip():
                    if name in line:
                        usr, pwd, quota_old= line.split('|')
                        line = usr + '|' + pwd + '|' + quota_new + '\n'
                    f2.write(line)
        os.remove(file)
        os.rename(file+'.bak',file)

    @staticmethod
    def checkQuota(file,dic):
        '''检查磁盘配额'''
        for n,p,q in sa.readInfo(file):
            if dic['name'] == n:
                dic['msg'] = '用户%s当前磁盘配额剩余：%s字节\n上传文件大小为：%s字节' % (dic['name'],q,dic['filesize'])
                num = int(q) - int(dic['filesize'])
                dic['flag'] = False if num < 0 else True
                if not dic['flag']:dic['msg'] = '%s用户磁盘配额不足！\n' % dic['name'] + dic['msg']
                dic['total'] = q
                dic['quota'] = str(num)
                return dic

    @classmethod
    def startGetFile(cls,conn,dic):
        '''客户端从服务器下载文件'''
        md5 = hashlib.md5() # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        total = dic['total_size']
        num = dic['exist_size']
        if dic['exist_size']:log.debug('文件上次已经下载了%s字节，开始断点下载！' % dic['exist_size'])
        with open(dic['file_path'],mode = 'rb') as f:
            f.seek(dic['exist_size']) # 将指针移动到指定位置开始读
            for line in f:
            # if line.strip():不能添加判断，要不导致发送的数据不全，文件内容不管是什么都给发送过去就行
                cls.mySend(conn,line)
                num += len(line) # 累计发送文件大小
                cls.processBar(num,total)
                md5.update(line)
        dic['server_md5'] = md5.hexdigest() # 自己发送数据的MD5值
        dic['client_md5'] = cls.myRecv(conn).decode() # 接收对方的MD5值
        dic['msg'] = 'MD5校验OK，文件传输成功！' if dic['client_md5'] == dic['server_md5'] else 'MD5不一致，文件传输失败！'
        dic['msg'] = dic['msg'] + '\n文件名：' + dic['file_path'] + '\nMD5值为：' + dic['server_md5']
        log.readAndWrite(dic['msg'])
        opt_dict = json.dumps(dic).encode('utf-8')
        cls.mySend(conn,opt_dict)
        return dic


    @classmethod
    def startPutFile(cls,conn,dic):
        '''从客户端上传文件到服务器'''
        md5 = hashlib.md5() # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        total = dic['total_size']
        num = dic['exist_size']
        if dic['exist_size']:log.debug('文件上次已经上传了%s字节，开始断点上传！' % dic['exist_size'])
        with open(dic['upload_file'],mode='ab') as f:
            while dic['filesize']>0:
                file_content = cls.myRecv(conn)
                dic['filesize'] -= len(file_content) # 剩余接收文件大小
                f.write(file_content)
                num += len(file_content) # 累计发送文件大小
                cls.processBar(num,total) # 进度条
                md5.update(file_content)
        dic['server_md5'] = md5.hexdigest() # 自己发送数据的MD5值
        dic['client_md5'] = cls.myRecv(conn).decode() # 接收对方的MD5值
        dic['msg'] = 'MD5校验OK，文件传输成功！' if dic['client_md5'] == dic['server_md5'] else 'MD5不一致，文件传输失败！'
        if not dic['msg'].find('成功') < 0:
            cls.updateQuota(ss.USER_FILE,dic['name'],dic['quota']) # 传输成功时更新磁盘配额
            dic['msg'] = dic['msg'] + '\n文件上传位置：' + dic['upload_file'] + '\nMD5值为：' + dic['server_md5'] + '\n磁盘配额剩余：%s字节' % dic['quota']
        log.readAndWrite(dic['msg'])
        opt_dict = json.dumps(dic).encode('utf-8')
        cls.mySend(conn,opt_dict)
        return dic


