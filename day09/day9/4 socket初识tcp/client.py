import socket

sk = socket.socket()  # 买手机

sk.connect(('192.168.36.202',9000))
while True:
    msg = sk.recv(1024).decode('utf-8')        # 字节 阻塞直到有数据发送过来
    if msg.upper() == 'Q': break
    print(msg) # 字节转字符串 decode
    msg_send = input('>>>')    # input写入的是字符串
    sk.send(msg_send.encode('utf-8')) # 发送的是字节,字符串转字节 encode
    if msg_send.upper() == 'Q': break
sk.close()