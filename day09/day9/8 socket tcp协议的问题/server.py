import socket
sk = socket.socket()
# sk.bind(('127.0.0.1',0-65535))
sk.bind(('127.0.0.1',9002))
sk.listen()

conn,addr = sk.accept()
msg = b'helloal7864862391862963496'  # 26helloal7864862391862963496
print(len(msg))  # 26
conn.send('0026')
conn.send(msg)
conn.send(b'5')
conn.send(b'world')
conn.close()
sk.close()

# 数据一旦黏在一起就会产生数据错误
# 怎么解决?

















