# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/10/13 下午3:47
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
conn,adrr = sk.accept()
ret = conn.recv(1024)
print(ret)
conn.send(b'HTTP/1.0 200 ok \r\n\r\n')
conn.send(b'<h1>hello word</h1>')
conn.close()
sk.close()
