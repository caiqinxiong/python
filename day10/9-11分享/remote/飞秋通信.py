from socket import *
updsocket = socket(type = SOCK_DGRAM)
addr = ("192.168.0.168",2425)
msg = input('>>>')
updsocket.sendto(("1:123456:eva:eva:32:%s"%msg).encode('gbk'),addr)
