# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午5:44
import socket
import struct
import time
sk = socket.socket()
sk.connect(('127.0.0.1',6666))

def my_recve(sk):
    pack_len = sk.recv(4)
    len_msg = struct.unpack('i',pack_len)[0]
    msg = sk.recv(len_msg).decode('utf-8')
    return msg

sk.recv(my_recve(sk))
msg = my_recve(sk)
print(msg)
msg = my_recve(sk)
print(msg)
sk.close()