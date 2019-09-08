# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/8 上午9:41
# import time
# import os
# from multiprocessing import Process
#
# def func(arg1,arg2):
#     print('子进程：',os.getpid())
#
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,2))
#     p.start()
#     time.sleep(1)
#     print('主进程',os.getpid())
import gevent,time
import socket
from gevent import monkey

def func(conn):
    while True:
        conn.send(b'hello')     # msg必须是字节类型
        message = conn.recv(1024)    # n是接受消息的最大字节数
        print(message)

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9001))
    sk.listen()
    while True:
        conn,addr = sk.accept()   # 接受客户端请求建立连接 -- 三次握手
        gevent.spawn(func,conn)
    conn.close()