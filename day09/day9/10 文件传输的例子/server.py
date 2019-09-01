# 接收文件
import json
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept()
file_dic = conn.recv(1024).decode('utf-8')
dic = json.loads(file_dic)

with open(dic['filename'],mode='wb') as f:
    while dic['filesize']>0:
        file_content = conn.recv(1024)
        dic['filesize'] -= len(file_content)
        f.write(file_content)
conn.close()
sk.close()