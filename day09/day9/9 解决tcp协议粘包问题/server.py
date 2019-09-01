import socket
import struct

def my_send(conn,msg):
    msgb = msg.encode('utf-8')
    len_msg = len(msgb)
    pack_len = struct.pack('i', len_msg)
    conn.send(pack_len)
    conn.send(msgb)

sk = socket.socket()
# sk.bind(('127.0.0.1',0-65535))
sk.bind(('127.0.0.1',9002))
sk.listen()

conn,addr = sk.accept()
msg1 = '你好'
msg2 = '吃了么'
my_send(conn,msg1)
my_send(conn,msg2)
conn.close()
sk.close()

# 数据一旦黏在一起就会产生数据错误
# 怎么解决?

















