# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:47

import sys,os
import time
import socket
import hashlib
import pickle
import subprocess
import socketserver
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from conf import settings

new=settings.NEW_FILENAME
class Myserver(socketserver.BaseRequestHandler):

    def recv_file(self):
        '''
        文件传输
        :return:
        '''
        conn=self.request
        a=str(conn.recv(1024),encoding='utf-8')
        file_size,file_name=a.split(',')
        new_file_name=os.path.join(new,file_name)
        if file_name in new:            #检测文件是否已存在，涉及断点续传
            has_recv=os.stat(new).st_size #计算临时文件大小
            conn.sendall(bytes(has_recv,encoding='utf-8'))
            with open(new_file_name,'ab') as f:  #追加模式
                while has_recv<=int(file_size):
                    data=conn.recv(1024)
                    f.write(data)
                    has_recv+=len(data)
        else:
            has_recv=0
            conn.sendall(bytes('s',encoding='utf-8')) # 客户端收到字符串s，从0开始发送
            with open(new_file_name,'wb') as f:
                while has_recv<=int(file_size):
                    data=conn.recv(1024)
                    f.write(data)
                    has_recv+=len(data)

    def command(self):
        '''
        执行命令
        :return:
        '''
        conn=self.request
        a=conn.recv(1024)
        ret=str(a,encoding='utf-8')
        ret2 = subprocess.check_output(ret, shell=True)
        r=divmod(len(ret2),1024)
        s=r[0]+1         #客户端需要接收的次数
        conn.sendall(bytes(str(s),encoding='utf-8'))
        conn.recv(1024)  #确认客户端收到需要接收的次数

        conn.sendall(ret2)

    def md5(self,pwd):
        '''
        对密码进行加密
        :param pwd: 密码
        :return:
        '''
        hash=hashlib.md5(bytes('xx7',encoding='utf-8'))
        hash.update(bytes(pwd,encoding='utf-8'))
        return hash.hexdigest()


    def login(self,usrname,pwd):
        '''
        登陆
        :param usrname: 用户名
        :param pwd: 密码
        :return:是否登陆成功
        '''
        conn=self.request
        s=pickle.load(open(settings.NAME_PWD,'rb'))
        if usrname in s:
             if s[usrname]==self.md5(pwd):        #和加密后的密码进行比较
                return True
             else:
                return False
        else:
            return False


    def regist(self,usrname,pwd):
        '''
        注册
        :param usrname: 用户名
        :param pwd: 密码
        :return:是否注册成功
        '''

        conn=self.request
        s=pickle.load(open(settings.NAME_PWD,'rb'))
        if usrname in s:
             return False
        else:
            s[usrname]=self.md5(pwd)
            mulu=os.path.join(settings.USER_FILE,usrname)
            os.makedirs(mulu,'a')
            pickle.dump(s,open(settings.NAME_PWD,'wb'))
            return True

    def before(self,usrname,pwd,ret):
        '''
        判断注册和登陆，并展示用户的详细目录信息，支持cd和ls命令
        :return:
        '''
        conn=self.request
        if ret=='1':
            r=self.login(usrname,pwd)
            if r:
                conn.sendall(bytes('y',encoding='utf-8'))
            else:
                conn.sendall(bytes('n',encoding='utf-8'))
        elif ret=='2':
            # print(usrname,pwd)
            r=self.regist(usrname,pwd)
            if r:
                conn.sendall(bytes('y',encoding='utf-8'))
            else:
                conn.sendall(bytes('n',encoding='utf-8'))
    def usr_file(self,usrname):
        '''
        展示用户的详细目录信息，支持cd和ls命令
        :param usrname: 用户名
        :return:
        '''
        conn=self.request
        conn.recv(1024)
        mulu=os.path.join(settings.USER_FILE,usrname)
        conn.sendall(bytes(mulu,encoding='utf-8'))
        while True:
            b=conn.recv(1024)
            ret=str(b,encoding='utf-8')
            try:
                a,b=ret.split(' ',1)
            except Exception as e:
                a=ret
            if a=='cd':
                if b=='..':
                    mulu=os.path.dirname(mulu)
                else:
                    mulu=os.path.join(mulu,b)
                conn.sendall(bytes(mulu,encoding='utf-8'))
            elif a=='ls':
                ls=os.listdir(mulu)
                print(ls)
                a=','.join(ls)
                conn.sendall(bytes(a,encoding='utf-8'))
            elif a=='q':
                break


    def handle(self):
        conn=self.request
        conn.sendall(bytes('welcome',encoding='utf-8'))
        b=conn.recv(1024)
        ret=str(b,encoding='utf-8')
        print(ret)
        conn.sendall(bytes('b ok',encoding='utf-8'))
        c=conn.recv(1024)
        r=str(c,encoding='utf-8')
        usrname,pwd=r.split(',')
        self.before(usrname,pwd,ret) #登陆或注册验证
        self.usr_file(usrname)  #展示用户的详细目录信息，支持cd和ls命令
        while True:
            a=conn.recv(1024)
            conn.sendall(bytes('收到a',encoding='utf-8'))
            ret=str(a,encoding='utf-8')
            if ret=='1':
                self.recv_file()
                # conn.sendall(bytes('file ok',encoding='utf-8'))
            elif ret=='2':
                self.command()
            elif ret=='q':
                break
            else:
                pass

if __name__=='__main__':
    sever=socketserver.ThreadingTCPServer(('127.0.0.1',9999),Myserver)
    sever.serve_forever()