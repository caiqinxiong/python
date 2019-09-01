import time
import socket
sk = socket.socket()



sk.connect(('127.0.0.1',9002))
for i in range(100000):i*2
msg1 = sk.recv(4)  # 2
print(msg1)
num = int(msg1.decode('utf-8'))
msg = sk.recv(num)
print(msg)
msg1 = sk.recv(1)
num = int(msg1.decode('utf-8'))
msg = sk.recv(num)
print(msg)
sk.close()













