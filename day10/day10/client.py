import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9001))  #  三次握手
while True:
    message = sk.recv(1024)
    print(message)
    sk.send(b'hello')
sk.close()