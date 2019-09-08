import socket
from threading import Thread
def func(conn):
    while True:
        conn.send(b'hello')     # msg必须是字节类型
        message = conn.recv(1024)    # n是接受消息的最大字节数
        print(message)

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9001))
    sk.listen()
    while True:
        conn,addr = sk.accept()   # 接受客户端请求建立连接 -- 三次握手
        Thread(target=func,args=(conn,)).start()
    conn.close()
