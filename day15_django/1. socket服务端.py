import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 8000))

sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    url = data.decode('utf-8').split()[1]
    if url == '/action/':
        ret = '动作'
    elif url == '/yizhi/':
        ret = '益智休闲'
    elif url == '/maoxian/':
        ret = '冒险'
    else:
        ret = '404 not found'
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
    conn.send(ret.encode('utf-8'))
    conn.close()
