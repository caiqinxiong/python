from gevent import socket
import gevent   # gevent在识别阻塞之后,会在遇到阻塞的时候自动识别

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
        conn,addr = sk.accept()
        gevent.spawn(func,conn)   # 开协程
    conn.close()

# 协程的好处 :可以开的个数更多
# 5 * 20 * 500 = 50000