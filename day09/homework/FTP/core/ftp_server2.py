# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:24
import sys,os,socket,hashlib,socketserver,json,time
from conf import settings as ss
from core import user
class MyServer(socketserver.BaseRequestHandler):
    print('等待链接...')
    '''
    FTP服务端类
    '''
    def auth(self,*args):
        '''
        用户登录认证函数
        1、接收客户端用户字典信息
        2、序列化字典信息
        3、调用Users类中get_user()函数
        4、判断用户是否有效
        5、发送认证信息至客户端
        :param args:
        :return:
        '''
        cmd = args[0]
        self.user_obj = users.Users(cmd['username'])
        auth_user = self.user_obj.get_user()
        if auth_user:
            if auth_user['password'] == cmd["password"]:
                if auth_user['status'] == 0:
                    self.request.send(b"ok")
                    #self.user_obj.update_status_close()
                    self.user_home = auth_user["home"]
                    self.user_type = auth_user["type"]
                else:
                    self.request.send(b"301")
                    print("\033[31;1m该用户已登录\033[0m")
            else:
                self.request.send(b'302')
                print("\033[31;1m密码错误\033[0m")
        else:
            self.request.send(b"300")
            print("\033[31;1m用户名不存在\033[0m")

    def put(self,*args):
        '''
        服务端发送文件给客户端
        1、判断文件是否存在
        2、获取文件总大小
        3、发送文件大小给客户端
        4、接收客户端下载文件请求
        5、开始循环发送文件给客户端
        6、发送完成后调用加密函数
        :param args:
        :return:
        '''
        cmd = args[0]
        file_path = os.path.join(ss.USER_HOME,self.user_home,'server_home',cmd["file_name"])
        if os.path.isfile(file_path):
            file_total_size = os.stat(file_path).st_size
            print("\033[32;1m获取文件大小:\033[0m",file_total_size)
            self.request.send(str(file_total_size).encode())
            self.request.recv(1024)
            print("开始发送文件")
            self.m = hashlib.md5()
            with open(file_path,'rb') as f:
                for line in f:
                    self.m.update(line)
                    self.request.send(line)
                self.encryption()
        else:
            self.request.send(b'305')
            print("文件不存在")

    def get(self,*args):
        '''
        服务端接收客户端发送文件函数
        1、接收客户端发送文件大小
        2、发送接收客户端文件请求
        3、开始接收文件
        4、跟踪文件接收并写入相应目录
        5、接收完成后调用加密函数
        :param args:
        :return:
        '''
        cmd = args[0]
        #print(cmd)
        file_path = os.path.join(ss.USER_HOME,self.user_home,"server_home",cmd["file_name"])
        print("\033[32;1m收到客户端发送文件大小：\033[0m", cmd["file_size"])
        self.request.send(b"ok")
        print("开始接收文件")
        file_total_size = cmd["file_size"]
        rever_size = 0
        self.m = hashlib.md5()
        with open(file_path,'wb') as f:
            while rever_size < file_total_size:
                if file_total_size - rever_size <1024:
                    size = file_total_size - rever_size
                else:
                    size = 1024
                data = self.request.recv(size)
                rever_size += len(data)
                self.m.update(data)
                f.write(data)
            self.encryption()

    def encryption(self):
        '''
        加密认证函数
        1、发送确认加密'400'请求
        2、发送服务端文件加密信息至客户端
        :return:
        '''
        client_back = self.request.recv(1024).decode()
        if client_back == "400":
            print("\033[32;1m确认加密请求\033[0m")
            server_file_md5 = self.m.hexdigest()
            self.request.send(server_file_md5.encode())
            print("\033[32;1m服务端文件加密:\033[0m", server_file_md5)
        else:
            print("\033[32;1m\n已取消加密.客户端文件接收完成\033[0m")

    def dir(self,*args):
        '''
        服务端查看目录文件信息函数
        1、序列化客户端字典信息
        2、popen()获取目录文件信息
        3、判断目录信息长度
        4、发送目录长度信息至客户端
        5、接收客户端回调请求
        6、发送目录信息至客户端
        :param args:
        :return:
        '''
        cmd = args[0]
        if cmd["object"] == 'home':
            file_name = 'user_home'
        else:
            file_name = 'server_home'
        file_path = os.path.join(ss.USER_HOME,self.user_home,file_name)
        res = os.popen("%s %s"%(cmd["action"],file_path)).read()
        print("in the dir:",res)
        if len(res) == 0:
            res = "has not output"
        self.request.send(str(len(res.encode())).encode())
        self.request.recv(1024)
        self.request.send(res.encode())


    def handle(self):
        '''
        与客户端交互函数（解析客户端操作指令）
        1、接收客户端链接信息
        2、接收客户端操作指令（action）需序列化
        3、反射操作指令
        :return:
        '''
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{}已链接".format(self.client_address))
                actin_dict = json.loads(self.data.decode())
                #print(actin_dict)
                print('in the handle',actin_dict["action"])
                if hasattr(self,str(actin_dict["action"])):
                    func = getattr(self,str(actin_dict["action"]))
                    func(actin_dict)
            except ConnectionResetError as e:
                print("%s客户端已断开%s"%(self.client_address,e))
                #self.user_obj.update_status_open()
                break

server = socketserver.ThreadingTCPServer((ss.IP_PORT),MyServer)    #支持多用户操作:ThreadingTCPServer
server.serve_forever()
