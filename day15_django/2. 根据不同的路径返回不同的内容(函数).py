import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 8000))

sk.listen()


def action(url):
    ret = "{}-{}".format(url, '动作')
    return ret


def yizhi(url):
    ret = "/{}-{}/".format(url, '益智休闲')
    return ret


def maoxian(url):
    ret = "zzzzz{}-{}".format(url, '冒险')
    return ret


while True:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    url = data.decode('utf-8').split()[1]
    if url == '/action/':
        ret = action(url)
    elif url == '/yizhi/':
        ret = yizhi(url)
    elif url == '/maoxian/':
        ret = maoxian(url)
    else:
        ret = '404 not found'
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
    conn.send(ret.encode('utf-8'))
    conn.close()
