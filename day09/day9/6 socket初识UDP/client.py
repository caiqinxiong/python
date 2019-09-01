import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'),('127.0.0.1',8001))
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()