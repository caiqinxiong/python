# -*- coding:utf-8 -*-
# Author:caiqinxiong
# 服务器端
import socket
server = socket.socket()
server.bind(('localhost',8080)) # 绑定要监听的端口
server.listen(5) # 监听5个
print('我要开始等电话')
while True:
    conn,addr = server.accept() # 等电话打进来,server.accept()返回两个值，分别赋值
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn,addr)
    print('电话来了')
    # date = server.recv(1024) # 用conn，不用server了
    while True:
        date = conn.recv(1024) #官方建议不要超过8192（8k）
        print('recv:',date)
        if not date:
            print('client has lost.....')
            break
        #server.send(date.upper())
        conn.send(date.upper())
server.close()
