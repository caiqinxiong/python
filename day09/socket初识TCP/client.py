# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午12:10

import socket
sk = socket.socket()
sk.connect(('192.168.36.158',6666))
while True:
    msg = sk.recv(1024)
    msg = msg.decode('utf-8')
    if msg.upper() == "Q":break
    print(msg)
    msg_send = input('>>>>')
    sk.send(msg_send.encode('utf-8'))
    if msg_send.upper() == "Q": break
sk.close()