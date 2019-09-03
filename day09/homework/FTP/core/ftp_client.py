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

    # def myRecv(self):
    #     '''解决粘包'''
    #     pack_len = self.sk.recv(4)
    #     len_msg = struct.unpack('i', pack_len)[0]
    #     msg = self.sk.recv(len_msg).decode('utf-8')
    #     return msg
    #
    # def mySend(self,msg):
    #     '''解决粘包'''
    #     msgb = msg.encode('utf-8')
    #     len_msg = len(msgb)
    #     pack_len = struct.pack('i', len_msg)
    #     self.sk.send(pack_len)
    #     self.sk.send(msgb)

    def getFileMD5(self,file):
        '''对文件做MD5校验'''
        md5 = hashlib.md5()
        with open(file,'rb') as f:
            for line in f:
                if line.strip():md5.update(line)
        return md5.hexdigest()

    def putFile(self,file_path):
        '''上传文件到服务器'''
        cn.putFile(self.sk,file_path,self.name)
        # self.sk.close()
        # 输入需要发送的文件,获取并发送文件大小
        # put_path = ss.USER_SERVER(self.name)
        # if not os.path.exists(put_path):os.makedirs(put_path)
        # file_name = os.path.join(put_path,os.path.basename(file_path))
        # file_size = os.path.getsize(file_path)
        # dic = {'filename':file_name,'filesize':file_size}
        # str_dic = json.dumps(dic)
        # # dic_b = str_dic.encode('utf-8')
        # # self.sk.send(dic_b)
        # self.mySend(str_dic)
        # with open(file_path,mode = 'r',encoding='utf-8') as f:
        #     # content = f.read()
        #     # self.sk.send(content)
        #     for line in f:
        #         if line.strip():self.mySend(line)
        # self.sk.close()
        # print(file_path)
        # print(file_name)
        # return file_name


    def getFile(self):
        '''接收从服务器下载的文件'''
        cn.getFile(self.sk)
        # file_dic = self.sk.recv(1024).decode('utf-8')
        # file_dic = self.myRecv()
        # dic = json.loads(file_dic)
        # with open(dic['filename'],mode='w' ,encoding='utf-8') as f:
        #     while dic['filesize']>0:
        #         # file_content = self.sk.recv(1024)
        #         file_content = self.myRecv()
        #         dic['filesize'] -= len(file_content)
        #         f.write(file_content)


    def processBar(self, num, total):
        rate = num / total
        rate_num = int(rate * 100)
        if rate_num == 100:
            r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
        else:
            r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush

f = FtpClient('caiqinxiong')
file_path = r'E:\python_test\python\day09\homework\FTP\log\2019-09-02-log'
# file_path = r'E:\文档\Python视频\年会舞蹈视频-20180202.mp4'
# file_path = r'E:\文档\Python视频\huangyanan\视频教程\小甲鱼零基础入门学习Python(全87集)\027集合：在我的世界里，你就是唯一.mp4'
file_name = f.putFile(file_path)
# print(f.getFileMD5(file_path))
# print(f.getFileMD5(file_name))
# if  f.getFileMD5(file_path) == f.getFileMD5(file_name):log.readAndWrite('%s\n上传至服务器成功\n%s' %(file_path,file_name))
#
# f.getFile()