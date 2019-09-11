# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:14
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
import os
error_code = {'400':'FILE IS NOT EXISTS'}

file_path = os.path.join(os.path.abspath('.'),'file')   #获取文件目录路径
'''服务端采用socketserver方式'''
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
           # print('new conn',self.client_address)
            data = self.request.recv(100)  #接收客户端请求
            if not data.decode():
                break
            elif data.decode().split()[0] == 'get':    #server判断是下载还是上传文件，get是下载
                offset = data.decode().split('|')[1]   #取出偏移量
                file = data.decode().split()[1].split('|')[0]   #取出要下载的文件名
                filename = os.path.join(file_path,file)
                read_len = 0
                if os.path.exists(filename) :   #判断是否有资源
                    with open(filename,'rb') as fd:
                        while True:
                            send_data = fd.read(1024)
                            read_len += len(send_data)  #记录读取数据长度
                            if send_data and read_len > int(offset):   #达到偏移量发送数据
                                ack_msg = "SEND SIZE|%s" % len(send_data)
                                self.request.send(ack_msg.encode())
                                client_ack = self.request.recv(50)
                                if client_ack.decode() =="CLIENT_READY_TO_RECV":
                                    self.request.send(send_data)
                            elif read_len <= int(offset):
                                continue
                            else:
                                send_data ='END'
                                self.request.send(send_data.encode())   #数据传输完毕发送finally信号
                                break
                else:
                    msg = '400'
                    self.request.send(msg.encode())
            elif data.decode().split()[0] == 'put':  #判断客户端是不是上传行为
                file = data.decode().split()[1]      #获取需要上传的文件名
                filename = os.path.join(file_path,file)   #定义文件路径
                log = "%s.%s" % (file,'log')           #指定记录偏移日志文件名
                logname = os.path.join(file_path,log)   #定义日志路径
                if os.path.exists(filename) and os.path.exists(logname):    #如果要上传的文件和日志文件同时存在，说明需要进行续传
                    with open(logname) as f:
                        offset = f.read().strip()   #读取偏移量
                else:
                    offset = 0          #表示不需要进行续传，直接从头开始传
                server_syn_msg = "offset %s" % offset   #把偏移信息发送给客户端
                self.request.send(server_syn_msg.encode())
                total_len = int(offset)    #获取已传输完的文件长度，即从这个位置开始接收新的数据
                while True:
                    receive_ack = self.request.recv(100)   #客户端接收到偏移信息后通知服务端要发送数据的长度信息，相当于一个ack
                    res_msg = receive_ack.decode().split('|')
                    if receive_ack.decode() == 'END':   #判断文件是否上传完成，完成后删掉偏移日志
                        os.remove(logname)
                        break
                    elif res_msg[0].strip() =='SEND SIZE':   #如果服务端收到了客户端发送过来的ack，给客户端返回一个syn信息，表示可以开始传数据了
                        res_size = res_msg[1]
                        self.request.send(b'CLIENT_READY_TO_RECV')
                        recv_data = self.request.recv(1024)  #接收数据
                        total_len += len(recv_data)   #记录接收数据长度
                    with open(filename,'ab') as fd:    #以追加的方式写入文件
                        fd.write(recv_data)
                    with open(logname,'w') as f:   #把已接收到的数据长度写入日志
                        f.write(str(total_len))
if __name__ == '__main__':
    host,port = "localhost",5000
    server = socketserver.ThreadingTCPServer((host,port),MyTCPHandler)
    server.serve_forever()   #开启服务端