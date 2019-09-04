# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:23
import sys,os,socket,hashlib,time,json
import struct
from conf import settings as ss
from core.log import Log as log
from core.common import Common as cn
class FtpClient:
    '''FTP客户端类'''
    def __init__(self,name):
        self.name = name
        self.sk = socket.socket()
        self.sk.connect(ss.IP_PORT)

    def putFile(self):
        '''上传文件到服务器'''
        file = input('请输入要上传到服务器的文件路径：').strip()
        if not os.path.isfile(file):
            cn.mySend(self.sk,b'error')
            return log.error('%s文件不存在!' % file)
        opt_dict = {'action':'getFile', 'file_path':file, 'name':self.name}
        dic_str = json.dumps(opt_dict)
        dic_b = dic_str.encode()
        cn.mySend(self.sk,dic_b) # 将执行命令发送给服务器，服务执行相应函数

        log.debug('开始上传%s到服务器！' % file)
        ret = cn.putFile(self.sk,file,ss.USER_SERVER,self.name)
        if not ret[-1].find('失败') < 0:
            log.warning(ret[-1])
        else:
            log.readAndWrite('%s\n文件已上传至服务器，路径如下：\n%s\nMD5值为：%s' % (ret[-1],ret[1],ret[0]))


    def getFile(self):
        '''接收从服务器下载的文件'''
        file = input('请输入要从服务器下载的文件路径：').strip()
        if not os.path.isfile(file):
            cn.mySend(self.sk,b'error')
            return log.error('%s文件不存在!' % file)
        opt_dict = {'action':'putFile', 'file_path':file, 'name':self.name}
        dic_str = json.dumps(opt_dict)
        dic_b = dic_str.encode()
        cn.mySend(self.sk,dic_b) # 将执行命令发送给服务器，服务执行相应函数

        log.debug('开始服务器中下载文件！' )
        ret = cn.getFile(self.sk)
        if not ret[-1].find('失败') < 0:
            log.warning(ret[-1])
        else:
            log.readAndWrite('%s\n文件已从服务器下载到：\n%s\nMD5值为：%s' % (ret[-1],ret[1],ret[0]))


f = FtpClient('caiqinxiong')
# file_path = r'E:\python_test\python\day09\homework\FTP\log\2019-09-02-log'
# file_path = r'E:\文档\Python视频\年会舞蹈视频-20180202.mp4'
# file_path = r'E:\文档\Python视频\huangyanan\视频教程\小甲鱼零基础入门学习Python(全87集)\027集合：在我的世界里，你就是唯一.mp4'
f.putFile()
# f.getFile()