# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/3 14:35
import struct
import json
import sys
import hashlib
from core.log import Log as log


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

    @classmethod
    def showMessage(cls, conn, opt_dict):
        cls.mySend(conn, opt_dict, True)  # 将执行命令发送给服务器，服务执行相应函数
        opt_dict = cls.myRecv(conn, True)  # 接收服务操作完成后返回的字典
        log.debug(opt_dict['msg'])  # 打印执行信息

    @staticmethod
    def processBar(num, total):
        '''打印进度条'''
        rate = num / total
        rate_num = int(rate * 100)
        bar = ('>' * rate_num, rate_num,)  # 展示的进度条符号
        r = '\r%s>%d%%\n' % bar if rate_num == 100 else '\r%s>%d%%' % bar
        sys.stdout.write(r)  # 覆盖写入
        return sys.stdout.flush  # 实时刷新

    @classmethod
    def startTransfer(cls, conn, dic, kind, file, mode, b_size=1024000):
        '''开始传输，提取上传下载公共代码'''
        md5 = hashlib.md5()  # 发送数据时，添加MD5校验，就不用再单独打开一次文件做校验了
        if dic['exist_size']: log.debug('文件上次已经%s了%s字节，开始断点续传！' % (kind, dic['exist_size']))
        with open(file, mode) as f:
            if kind == '上传': f.seek(dic['exist_size'])  # 将指针移动到指定位置开始读
            while dic['filesize'] > 0:
                if kind == '上传':
                    line = f.read(b_size)
                    conn.send(line)  # 发生粘包也没有关系，反正最后把文件传完就行
                elif kind == '下载':
                    line = conn.recv(b_size)  # 发生粘包也没有关系，反正最后把文件传完就行
                    f.write(line)
                dic['exist_size'] += len(line)  # 累计发送文件大小，传输进度条用
                dic['filesize'] -= len(line)  # 退出循环用
                cls.processBar(dic['exist_size'], dic['total_size'])
                md5.update(line)
        clinet_md5 = md5.hexdigest()  # 自己的MD5值
        cls.mySend(conn, clinet_md5.encode('utf-8'))  # 发送MD5值给服务器做校验
        opt_dic = cls.myRecv(conn, True)  # 接收校验结果，返回字典
        log.readAndWrite(opt_dic['msg'])
        return opt_dic

    @classmethod
    def startGetFile(cls, conn, dic):
        '''接收文件，客户端从服务器下载文件'''
        return cls.startTransfer(conn, dic, kind='下载', file=dic['download_file'], mode='ab')

    @classmethod
    def startPutFile(cls, conn, dic):
        '''发送文件，从客户端发送文件到服务器'''
        return cls.startTransfer(conn, dic, kind='上传', file=dic['file_path'], mode='rb')



