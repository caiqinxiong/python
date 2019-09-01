import time
import socket
import struct
sk = socket.socket()

def my_recv(sk):
    pack_len = sk.recv(4)
    len_msg = struct.unpack('i', pack_len)[0]
    msg = sk.recv(len_msg).decode('utf-8')
    return msg

sk.connect(('127.0.0.1',9002))
for i in range(100000):i*2
msg = my_recv(sk)
print(msg)
msg = my_recv(sk)
print(msg)
sk.close()













