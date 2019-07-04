# -*- coding:utf-8 -*-
# Author:caiqinxiong
# 客户端
import socket
client = socket.socket() # 声明socketl类型，同时生成socket连接对象
client.connect(('localhost',8080))
while True:
    msg = input('>>>>>:').strip()
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))
    #client.send('发生中文测试'.encode('utf-8')) # 所有的数据发送／接收都得用byte方式
    date = client.recv(1024)# 收1024个字节1k
    print('recv:',date.decode())

client.close()
