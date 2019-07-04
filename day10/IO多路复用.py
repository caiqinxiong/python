# -*- coding:utf-8 -*-
# Author:caiqinxiong
import select
import socket
import Queue

server = socket.socket()
server.bind(('localhost',666))
server.listen(1000)

server.setblocking(False) # recv没数据不阻塞
