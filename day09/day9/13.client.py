import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9001))
while True:
    ret = sk.recv(1024)
    print(ret)
sk.close()