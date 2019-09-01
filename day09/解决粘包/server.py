# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/1 下午5:44
import socket
import struct
sk = socket.socket()
sk.bind(('127.0.0.1',6666))
sk.listen()

def my_send(conn,msg):
    '''解决粘包'''
    msg_byte = msg.encode('utf-8')
    msg_len = len(msg_byte)
    pack_len = struct.pack('i',msg_len)
    conn.send(pack_len)
    conn.send(msg_byte)

conn,addr = sk.accept()
msg1 = '哈哈哈'
msg2 = '呵呵呵'
my_send(conn,msg1)
my_send(conn,msg2)
conn.close()
sk.close()

