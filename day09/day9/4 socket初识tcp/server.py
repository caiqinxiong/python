import socket

sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)   # 买手机
# family = socket.AF_INET 当前基于网络通信的
# type = socket.SOCK_STREAM 默认是tcp协议
sk.bind(('192.168.36.202',9000))    # 装上电话卡
sk.listen()                     # 开机
while True:
    conn,addr = sk.accept() # 等电话,等待客户端来链接我
        # conn 就是server和客户端建立起来的一个连接
    while  True:
        msg_send = input('>>>')
        conn.send(msg_send.encode('utf-8')) # 接了电话并说了一句hello
        if msg_send.upper() == 'Q': break
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q': break
        print(msg)
    conn.close()         # 挂电话
sk.close()           # 关手机

# 无论在server 还是 client 只要输入q 就两边断开连接 - 挂电话