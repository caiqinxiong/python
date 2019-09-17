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

    @staticmethod
    def mySend(conn, msgb, dic=False):
        '''发送数据时，解决粘包问题'''
        if dic: msgb = json.dumps(msgb).encode('utf-8')
        len_msg = len(msgb)
        pack_len = struct.pack('i', len_msg)
        conn.send(pack_len)
        conn.send(msgb)

    @staticmethod
    def myRecv(conn, dic=False):
        '''接收数据时，解决粘包问题'''
        pack_len = conn.recv(4)  # struct机制，在发送数据前，加上固定长度4字节的头部
        len_msg = struct.unpack('i', pack_len)[0]  # 解包，得到元组。
        msg_b = conn.recv(len_msg)
        if dic: msg_b = json.loads(msg_b.decode('utf-8'))
        return msg_b

    @staticmethod
    def processBar(num, total):
        '''打印进度条'''
        rate = num / total
        rate_num = int(rate * 100)
        bar = ('>' * rate_num, rate_num,)  # 展示的进度条符号
        r = '\r%s>%d%%\n' % bar if rate_num == 100 else '\r%s>%d%%' % bar
        sys.stdout.write(r)  # 覆盖写入
        return sys.stdout.flush  # 实时刷新

    @staticmethod
    def updateQuota(file, name, quota_new):
        '''更新磁盘配额'''
        with open(file, mode='r', encoding='utf-8') as f1, open(file + '.bak', mode='w', encoding='utf-8') as f2:
            for line in f1:
                if line.strip():
                    if name in line:
                        usr, pwd, quota_old = line.split('|')
                        line = usr + '|' + pwd + '|' + quota_new + '\n'
                    f2.write(line)
        os.remove(file)
        os.rename(file + '.bak', file)

    @staticmethod
    def checkQuota(file, dic):
        '''检查磁盘配额'''
        for n, p, q in sa.readInfo(file):
            if dic['name'] == n:
                dic['msg'] = '用户%s当前磁盘配额剩余：%s字节\n上传文件大小为：%s字节' % (dic['name'], q, dic['filesize'])
                num = int(q) - int(dic['filesize'])
                dic['flag'] = False if num < 0 else True
                if not dic['flag']: dic['msg'] = '%s用户磁盘配额不足！\n' % dic['name'] + dic['msg']
                dic['total'] = q
                dic['quota'] = str(num)
                return dic

    @classmethod
    def startTransfer(cls, conn, dic, kind, file, mode, b_size=1024000):
        '''开始传输，提取上传下载公共代码'''
        md5 = hashlib.md5()  # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        if dic['exist_size']: log.debug('文件上次已经%s了%s字节，开始断点续传！' % (kind, dic['exist_size']))
        with open(file, mode) as f:
            if kind == '下载': f.seek(dic['exist_size'])  # 将指针移动到指定位置开始读
            while dic['filesize'] > 0:
                if kind == '下载':
                    line = f.read(b_size)
                    conn.send(line)  # 发生粘包也没有关系，反正最后把文件传完就行
                elif kind == '上传':
                    line = conn.recv(b_size)  # 发生粘包也没有关系，反正最后把文件传完就行
                    f.write(line)
                dic['exist_size'] += len(line)  # 累计发送文件大小，传输进度条用
                dic['filesize'] -= len(line)  # 退出循环用
                cls.processBar(dic['exist_size'], dic['total_size'])
                md5.update(line)
        dic['server_md5'] = md5.hexdigest()  # 自己发送数据的MD5值
        dic['client_md5'] = cls.myRecv(conn).decode('utf-8')  # 接收对方的MD5值
        dic['msg'] = 'MD5校验OK，文件传输成功！' if dic['client_md5'] == dic['server_md5'] else 'MD5不一致，文件传输失败！'
        if not dic['msg'].find('成功') < 0 and kind == '上传':
            cls.updateQuota(ss.USER_FILE, dic['name'], dic['quota'])  # 传输成功时更新磁盘配额
            dic['msg'] = dic['msg'] + '\n文件上传位置：' + dic['upload_file'] + '\nMD5值为：' + dic['server_md5'] + '\n磁盘配额剩余：%s字节' % dic['quota']
        elif not dic['msg'].find('成功') < 0 and kind == '下载':
            dic['msg'] = dic['msg'] + '\n文件下载位置：' + dic['download_file'] + '\nMD5值为：' + dic['server_md5']
        log.readAndWrite(dic['msg'])
        cls.mySend(conn, dic, True)
        return dic


    @classmethod
    def startGetFile(cls, conn, dic):
        '''客户端从服务器下载文件'''
        return cls.startTransfer(conn, dic, kind='下载', file=dic['file_path'], mode='rb')


    @classmethod
    def startPutFile(cls, conn, dic):
        '''从客户端上传文件到服务器'''
        return cls.startTransfer(conn, dic, kind='上传', file=dic['upload_file'], mode='ab')

