import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
ret = conn.recv(1024)
conn.send(b'HTTP/1.1 200 OK \r\n\r\n')
conn.send(b'<h1>hello,world</h1>')
print(ret)
conn.close()
sk.close()