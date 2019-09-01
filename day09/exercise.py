# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 上午9:26
# 接收文件
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept()
file_size = int(conn.recv(1024).decode('utf-8'))
file_content = conn.recv(file_size)
with open('xxx.mp4',mode='wb') as f:
    f.write(file_content)
conn.close()
sk.close()