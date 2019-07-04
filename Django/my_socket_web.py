# -*- coding:utf-8 -*-
# Author:caiqinxiong

import socket

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# 基于IPV4，tcp/ip
    # 强行结束被占用的端口
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(('localhost',8000))
    sock.listen(5)
    while True:
        # 等待浏览器访问
        conn, addr = sock.accept()
        # 接收浏览器发送过来的请求
        data = conn.recv(1024)
        print(data)
        print(addr)

        # 给浏览器返回内容
        conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html; charset:utf-8\r\n\r\n')
        #conn.send("加油吧，小伙子！！".encode("utf-8"))
        conn.send("<h1 style='color:red'>加油吧，小伙子！！</h1>".encode("gbk"))

        # 关闭和浏览器创建的链接
        conn.close()

if __name__ == '__main__':
    main()

