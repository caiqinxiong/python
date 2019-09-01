# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午3:49
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',6666))
while True:
    conn,adrr = sk.recvfrom(1024)
    conn = conn.decode('utf-8')
    if conn.upper() == 'Q':
        print(adrr,'要挂电话了'  )
        sk.sendto(b'q',adrr)
        continue
    print(conn)
    msg = input('>>>>')
    sk.sendto(msg.encode('utf-8'),adrr)
sk.close()