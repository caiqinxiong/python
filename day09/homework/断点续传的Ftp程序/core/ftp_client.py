# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:46

import sys
import time
import os
import socket
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from conf import settings

def send_file(file_path):
    '''
    发送文件
    :param file_name:文件名
    :return:
    '''
    size=os.stat(file_path).st_size
    file_name=os.path.basename(file_path)
    obj.sendall(bytes(str(size)+','+file_name,encoding='utf-8')) #发送文件大小和文件名
    ret=obj.recv(1024)   #接收已经传了多少
    r=str(ret,encoding='utf-8')
    if r=='s': #文件不存在，从头开始传
        has_send=0
    else:   #文件存在
        has_send=int(r)

    with open(file_path,'rb') as f:
        f.seek(has_send) #定位到已经传到的位置
        while has_send<size:
            data=f.read(1024)
            obj.sendall(data)
            has_send+=len(data)
            sys.stdout.write('\r')  #清空文件内容
            time.sleep(0.2)
            sys.stdout.write('已发送%s%%|%s' %(int(has_send/size*100),(round(has_send/size*40)*'★')))
            sys.stdout.flush()   #强制刷出内存
        print("上传成功\n")

def command(command_name):
    '''
    执行命令
    :param command_name:
    :return:
    '''
    obj.sendall(bytes(command_name,encoding='utf-8'))
    ret=obj.recv(1024)  #接收命令需要接收的次数
    obj.sendall(bytes('收到次数',encoding='utf-8'))
    r=str(ret,encoding='utf-8')
    for i in range(int(r)): #共需要接收int(r)次
        ret=obj.recv(1024)  #等待客户端发送
        r=str(ret,encoding='GBK')
        print(r)

def login(usrname,pwd):
    '''
    登陆
    :param usrname:用户名
    :param pwd:密码
    :return:是否登陆成功
    '''
    obj.sendall(bytes(usrname+','+pwd,encoding='utf-8'))
    ret=obj.recv(1024)
    r=str(ret,encoding='utf-8')
    if r=='y':
        return 1
    else:
        return 0

def regist(usrname,pwd):
    '''
    注册
    :param usrname:用户名
    :param pwd:密码
    :return:是否注册成功
    '''
    obj.sendall(bytes(usrname+','+pwd,encoding='utf-8'))
    ret=obj.recv(1024)
    r=str(ret,encoding='utf-8')
    if r=='y':
        return 1
    else:
        return 0
def before(usrname,pwd):
    '''
    选择登陆或注册，展示用户的详细目录信息，支持cd和ls命令
    :return:
    '''
    a=input('请选择1.登陆 2.注册')
    obj.sendall(bytes(a,encoding='utf-8'))
    obj.recv(1024)
    if a=='1':
        ret=login(usrname,pwd)
        if ret:
            print('登陆成功')
            return 1
        else:
            print('用户名或密码错误')
            return 0
    elif a=='2':
        ret=regist(usrname,pwd)
        if ret:
            print('注册成功')
            return 1
        else:
            print('用户名已存在')
            return 0
def usr_file(usrname):
    obj.sendall(bytes('打印用户文件路径',encoding='utf-8'))
    ret=obj.recv(1024)  #等待客户端发送
    r=str(ret,encoding='utf-8')
    print(r)
    while True:
        a=input('输入cd切换目录，ls查看目录详细信息，q退出>:')

        obj.sendall(bytes(a,encoding='utf-8'))
        if a=='q':
            break
        else:
            ret=obj.recv(1024)  #等待客户端发送
            r=str(ret,encoding='utf-8')
            if len(r)==1:#判断是cd结果还是ls的结果（ls只有一个子目录也可以直接打印）
                print(r)
            else:
                li=r.split(',')
                for i in li:
                    print(i)  #打印每一个子目录

def main(usrname,pwd):
    ret=obj.recv(1024)  #等待客户端发送
    r=str(ret,encoding='utf-8')
    print(r)
    # result=before(usrname,pwd)#登陆或注册
    # if result:
    if True:
        usr_file(usrname)
        while True:
            a=input('请选择1.传文件 2.执行命令 q退出:')
            obj.sendall(bytes(str(a),encoding='utf-8'))
            ret=obj.recv(1024) #确认是否收到a
            r=str(ret,encoding='utf-8')
            print(r)
            if a=='1':
                b=input('请输入文件路径（测试版路径为：f.png）:')
                # b='f.png'
                if os.path.exists(b):
                    send_file(b)
                    obj.sendall(bytes('hhe',encoding='utf-8'))
                    # obj.recv(1024)
            elif a=='2':
                b=input('请输入command:')
                command(b)
            elif a=='q':
                break
            else:
                print('输入错误')

    obj.close()

if __name__ == '__main__':
    obj=socket.socket() #创建客户端socket对象
    obj.connect(('127.0.0.1',9999))
    usrname=input('请输入用户名')
    pwd=input('请输入密码')
    main(usrname,pwd)