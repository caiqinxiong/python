# -*- coding:utf-8 -*-
# Author:caiqinxiong
import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',1111)) # 要两个括号，里面是元组
server.listen()
while True:
    conn,arr = server.accept()
    print("new conn:",arr)
    while True:
        print('等待新指令')
        data = conn.recv(1024)
        if not data:
            print("客户端已断开！")
            break

        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,'br')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode()) # send file size
            conn.recv(1024) # wait for client ack
            for line in f:
                m.updat(line)
                conn.send(line)
            print("file_md5:",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode()) # send the md5
        print('send done!')

server.close()
