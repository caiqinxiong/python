# -*- coding:utf-8 -*-
# Author:caiqinxiong
import socket
client = socket.socket()
client.connect(('localhost',1111)) # 要两个括号，里面是元组
while True:
    res = input('>>>>:').strip()
    if len(res) == 0: continue
    client.send(res.encode('utf-8'))
    cmd_res_size = client.recv(1024) # 接收命令结果长度
    print('命令结果大小为：',cmd_res_size)
    client.send('准备好接收了，可以发送数据了。'.encode('utf-8')) #跟服务器进去确认，避免发生粘包
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) # 每次接收的数据可能小于1024，所以必须用len来判断。
        received_data += data # 接收数据累加
    else:
        print('数据接收完成，大小为：',received_size)
        print(received_data.decode())

client.close()
