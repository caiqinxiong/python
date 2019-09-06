# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:13
import socket
import os,sys

receive_file_path = os.path.abspath(os.path.join(os.path.abspath('.'),'receive_file'))  #指定文件目录路径
error_code = {'400':'FILE IS NOT EXISTS'}
'''使用类的方式，方便反射'''
class SOCKET(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    def socket_obj(self):
        sk = socket.socket()
        sk.connect((self.ip,self.port))
        return sk
    def get(self):  #get表示从服务端下载文件到本地
        conn = self.socket_obj()  #生成对象
        user_input = input('get filename:')   #指定输入命令格式 get filename
       # print(msg,type(msg))
        filename = user_input.split()[1]   #获取文件名
        file = os.path.join(receive_file_path,filename)   #下载文件的绝对路径
        logname = '%s.%s' % (filename,'log')    #生成日志名
        log = os.path.join(receive_file_path,logname)   #偏移量日志的绝对路径
        if os.path.exists(log) and os.path.exists(file):    #判断是否需要续传，如果需要就读出偏移量
            with open(log) as f:
                offset = f.read().strip()
        else:
            offset = 0                   # 否则偏移量置0
        msg = "%s|%s" %(user_input,offset)
        conn.send(msg.encode())
        total_length = int(offset)           #记录传输完成了多少
        while True:
            server_ack_msg = conn.recv(100)   #接收第一个ack
            if server_ack_msg.decode().strip() == '400':    #如果ftp服务器没有这个资源，返回错误
                print('400', error_code['400'])
                conn.close()
                break
            elif server_ack_msg.decode().strip() == 'END':   #传输完成，ftp server返回字段，并删除偏移量日志
                conn.close()
                os.remove(log)
                break
            res_msg = server_ack_msg.decode().split('|')  #接收server的syn和传输数据大小的信息
            if res_msg[0].strip() == "SEND SIZE":
                res_size = int(res_msg[1])
                conn.send(b'CLIENT_READY_TO_RECV')   #给server返回ack
                receive_data = conn.recv(1024)    #接收server的数据
                total_length += len(receive_data)  #记录接收到了多少数据
               # print(receive_data.decode())
              # print(total_length)
            with open(file,'ab') as fd:   #以追加的方式写文件
                fd.write(receive_data)
            with open(log,'w') as f:     #把已接收数据长度写进日志
                f.write(str(total_length))

    def put(self):  #put表示上传文件至服务端
        conn = self.socket_obj() #生成对象
        msg = input('put filename:')   #指定命令输入格式，put filename
        filename = os.path.join(receive_file_path, msg.split()[1])   #生成上传文件路径
        if  os.path.exists(filename):  #判断文件存在与否，不存在返回错误
            conn.send(msg.encode())   #发送文件行为与文件名至服务端
            server_syn_msg = conn.recv(100)  #接收服务端发送的偏移量信息
            offset = server_syn_msg.decode().split()[1]
            read_length = 0   #重置需要读取文件的长度
            with open(filename,'rb') as fd:
                while True:
                    send_data = fd.read(1024)   #开始读取文件，每次读取1024字节
                    read_length += len(send_data)  #记录读取数据长度
                    if send_data and read_length> int(offset):  #和服务端发送的偏移量进行比较，只有数据不为空和读到超过偏移量才会发送数据
                        ack_msg = "SEND SIZE|%s" %len(send_data)  #给服务端发送本次要发送数据的长度，相当于一个syn
                        conn.send(ack_msg.encode())
                        client_ack = conn.recv(100) #接收到服务端发送的ack确认信息，收到之后开始传输数据
                        if client_ack.decode() =='CLIENT_READY_TO_RECV':
                            conn.send(send_data)
                    elif read_length <= int(offset):  #如果读取到的数据长度没到偏移量就继续循环读取文件
                        continue
                    else:
                        send_data = 'END'   #文件已经读完，表示已经全部发送完成，给服务端发送信息说明客户端已经发送完成
                        conn.send(send_data.encode())
                        break
        else:
            print('400', error_code['400'])


if __name__ == '__main__':
    c = SOCKET('127.0.0.1',5000)

    if hasattr(c,sys.argv[1]):
        func = getattr(c,sys.argv[1])
        func()