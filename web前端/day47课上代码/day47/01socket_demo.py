# web本质 示例

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8000))
sk.listen(5)

while 1:
    conn, addr = sk.accept()
    data = conn.recv(1024)  # 收消息
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 按照HTTP协议的格式发消息
    # 从文件读取\
    with open("data.html", "rb") as f:
        msg = f.read()
    conn.send(msg)  # 发消息
    conn.close()


