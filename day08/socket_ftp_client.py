# -*- coding:utf-8 -*-
# Author:caiqinxiong
import socket,hashlib
client = socket.socket()
client.connect(('localhost',1111)) # 要两个括号，里面是元组
while True:
    cmd = input('>>>>:').strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('server_response:',server_response)
        client.send(b'ready to rece file')
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[-1]
        f = open(filename + "_new","wb")
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size - received_size > 1024: # 要收不止一次
                size = 1024
            else:# 最后一次了，剩多少，收多少
                size = file_total_size - received_size
                print('last receive :',size)
            data = client.recv(size)
            received_size += len(data) # 每次接收的数据可能小于1024，所以必须用len来判断。
            m.update(data)
            f.write(data)
        else:
            client_file_md5 = m.hexdigest()
            print('数据接收完成，大小为：',received_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print("server_file_md5",server_file_md5)
        print("client_file_md5",client_file_md5)

client.close()
