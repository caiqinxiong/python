# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午12:07
import  socket
sk = socket.socket()
sk.bind(('192.168.36.158',6666))
sk.listen()
while True:
    conn,adrr = sk.accept()
    while True:
        msg_send = input('>>>').encode('utf-8')
        conn.send(msg_send)
        if msg_send.upper() == "Q":break
        msg = conn.recv(1024)
        msg = msg.decode('utf-8')
        if msg.upper() == "Q": break
        print(msg)
    conn.close()
sk.close()