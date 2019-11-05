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


def home(url):
    ret = "{}-{}".format(url, '家')
    return ret


list1 = [
    ('/action/', action),
    ('/yizhi/', yizhi),
    ('/maoxian/', maoxian),
    ('/home/', home),
]

while True:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    url = data.decode('utf-8').split()[1]

    func = None
    for i in list1:
        if url == i[0]:
            func = i[1]
            break
    if func:
        ret = func(url)
    else:
        ret = '404 not found'
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')
    conn.send(ret.encode('utf-8'))
    conn.close()
