# -*- coding:utf-8 -*-
# Author:caiqinxiong
import socket,os,time
server = socket.socket()
server.bind(('localhost',1111)) # 要两个括号，里面是元组
server.listen()
while True:
    conn,arr = server.accept()
    print("new conn:",arr)
    while True:
        print('等待新指令')
        data = conn.recv(1024)
        if not data:
            print("客户端已断开！")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read() # data.decode()接收字符串，执行结果也是字符串
        print('发送之前的数据大小：',len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no uoput!'
        conn.send(str(len(cmd_res.encode())).encode('utf-8')) # 先发数据大小给客户端
        #time.sleep(0.5) # 两条命令连着发送执行，避免粘包，但是这种方法不可取
        client_ack = conn.recv(1024) # 等待客户端确认，客户端自动确认接收到了数据
        conn.send(cmd_res.encode('utf-8')) # 将数据发送给客户端
        print('数据发送完成！')

server.close()
