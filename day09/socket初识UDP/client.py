# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午3:52
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'),('127.0.0.1',6666))
    conn,adrr = sk.recvfrom(1024)
    conn = conn.decode('utf-8')
    if conn.upper() == 'Q':break
    print(conn)
sk.close()