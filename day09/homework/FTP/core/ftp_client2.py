# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:23
#-*- Coding:utf-8 -*-
# Author: D.Gray
import sys,os,socket,hashlib,time,json
from conf import settings as ss
from core import user
class FtpClient:
    '''FTP客户端类'''
    sk = socket.socket()
    sk.connect(ss.IP_PORT)

    def __init__(self):
        '''
        构造函数
        '''
        self.help_info = """\033[33;1m
                    请用'put'+'空格'+'文件名'的格式下载文件
                    请用'get'+'空格'+'文件名'的格式上传文件
                    请用'cd'+'空格'+'目录名'的格式进入家目录下的子文件夹
                    请用'cd'+'空格'+'..'的格式返回上级目录
                    请用'mkdir'+'空格'+'目录名'的格式创建家目录的文件夹
                    输入'dir'+'空格'+'home'查看用户家目录
                    输入'dir'+'空格'+'server'查看用户服务端家目录
            \033[0m"""
        if self.auth():
            self.start()

    def auth(self):
        '''
        用户登录认证函数
        1、用户输入账号密码
        2、序列化用户信息字典发送给服务端
        3、接收服务端用户登录认证消息
        4、认证成功返回True给构造函数
        5、用户进入start（）函数进行指令操作
        :return:
        '''
        while True:
            username = input("请输入账户名>>>:").strip()
            password = input('请输入用户密码>>>:').strip()
            #auth = 'auth %s %s'%(username,password)
            mesg = {
                "action":'auth',
                "username":username,
                "password":password
            }
            self.client.send(json.dumps(mesg).encode())
            self.user_obj = users.Users(username)
            back_res = self.client.recv(1024).decode()
            if back_res == 'ok':
                print("\033[32;1m认证成功\033[0m")
                user = self.user_obj.get_user()
                self.user_name = user["username"]
                self.user_type = user["type"]
                self.user_path = user['home']
                self.disk_quota = user["disk_quota"]
                self.pwd_path = os.path.join(ss.USER_HOME,self.user_path,"user_home") #定义一个默认路径
                return True
            elif back_res == "302":
                print("\033[31;1m密码错误\033[0m")
            elif back_res == "301":
                print("\033[31;1m该用户已登录\033[0m")
            else:
                print("\033[31;1m用户不存在\033[0m")

    def start(self):
        '''
        用户操作函数
        1、用户输入操作指令
        2、判断操作指令是否有效
        3、反射指令
        :return:
        '''
        while True:
            user_inport = input("%s>>>:"%(self.user_name)).strip()
            if len(user_inport) == 0 :continue
            user_inport = user_inport.split()
            if user_inport[0] == 'q':
                break
            if hasattr(self,user_inport[0]):
                func = getattr(self,user_inport[0])
                func(user_inport)
            else:
                print("\033[31;1m请输入有效指令:\033[0m",self.help_info)
                continue

    def put(self,cmd):
        '''
        下载服务端文件函数
        1、接收服务端回调信息（305 = 服务端文件不存在或下载文件大小）
        2、判断磁盘配额和文件大小
        3、接收服务端回调信息
        4、开始接收文件并打印进度条
        5、加密认证
        6、重新计算磁盘配额  调用Users类中update_disk_quota（）方法将最新磁盘配额参数重新写入用户文件中
        :param cmd:
        :return:
        '''
        if len(cmd) < 2:
            print("\033[31;1m请输入有效指令:\033[0m", self.help_info)
        else:
            '''
            下载服务端文件
            '''
            mesg = {
                "action": cmd[0],
                "file_name": cmd[1],
                "disk_quota": self.disk_quota
            }
            self.client.send(json.dumps(mesg).encode())
            server_back = self.client.recv(1024).decode()
            print("\033[32;1m收到服务器回调：\033[0m",server_back)
            if server_back == '305':
                print("\033[31;1m文件不存在\033[0m")
            else:
                file_total_size = int(server_back)
                print("\033[32;1m下载文件总大小:\033[0m", file_total_size)
                print("\033[32;1m磁盘配额还剩：%sM\033[0m" % mesg["disk_quota"])
                if file_total_size >= mesg["disk_quota"] * (2 ** 20):
                    print('\033[31;1m磁盘配额不够无法下载文件\033[0m')
                else:
                    revered_size = 0
                    # file_path = os.path.join(setting.USER_HOME,self.user_path,"user_home",cmd[1])
                    file_path = os.path.join(self.pwd_path,cmd[1])
                    print('in the put_pwd_path:',file_path)
                    self.client.send(b"ok")
                    self.m = hashlib.md5()
                    i = 0
                    with open(file_path,'wb') as f:
                        while revered_size < file_total_size:
                            if file_total_size - revered_size < 1024:
                                size = file_total_size - revered_size
                            else:
                                size = 1024
                            data = self.client.recv(size)
                            revered_size += len(data)
                            '''
                            打印进度条
                            '''
                            str1 = "已接受 %sByte"%revered_size
                            str2 = '%s%s'%(round((revered_size/file_total_size)*100,2),'%')
                            str3 = '[%s%s]'%('*'*i,str2)
                            sys.stdout.write('\033[32;1m\r%s%s\033[0m'%(str1,str3))
                            sys.stdout.flush()
                            i += 2
                            time.sleep(0.3)
                            '''
                            加密认证
                            '''
                            self.m.update(data)
                            f.write(data)
                        self.encryption()
                        '''
                        磁盘配额
                        '''
                        new_disk_quota = round((mesg["disk_quota"] * (2 ** 20) - file_total_size) / (2 ** 20), 2)
                        # mesg["disk_quota"]* (2 ** 20)  将用户文件中磁盘参数转成相应的Bytes数值
                        self.user_obj.update_disk_quota(new_disk_quota)
                        print("\033[32;1m磁盘配额还剩：%sM\033[0m"%new_disk_quota)

    def get(self,cmd):
        '''
        客户端上传文件至服务端函数
        1、判断指令格式是否正确
        2、上传文件或文件路径是否有效和存在
        3、获取文件大小
        4、判断磁盘配额是否大于文件大小
        5、获取服务端上传文件回调请求
        6、发送文件并打印进度条
        7、加密认证
        8、重新计算磁盘配额  调用Users类中update_disk_quota（）方法将最新磁盘配额参数重新写入用户文件中
        :param cmd:
        :return:
        '''
        if len(cmd) < 2:
            print("\033[31;1m请输入有效指令:\033[0m", self.help_info)
        else:
            '''
            上传文件
            '''
            file_path = os.path.join(self.pwd_path,cmd[1])
            if os.path.isfile(file_path):
                file_total_size = os.stat(file_path).st_size
                mesg = {
                    "action": cmd[0],
                    "file_name": cmd[1],
                    "disk_quota": self.disk_quota,
                    "file_size" : file_total_size
                }
                print("\033[32;1m磁盘配额还剩：%sM\033[0m" % mesg["disk_quota"])
                if file_total_size >= mesg["disk_quota"]*(2**20):
                    print("\033[31;1m磁盘配额不够无法上传文件\033[0m")
                else:
                    self.client.send(json.dumps(mesg).encode())
                    print("\033[32;1m上传文件总大小:\033[0m", file_total_size)
                    self.client.recv(1024)
                    print("开始发送文件")
                    self.m = hashlib.md5()
                    send_size = 0
                    i = 0
                    with open(file_path,'rb')as f:
                        while send_size < file_total_size:
                            if file_total_size - send_size <1024:
                                size = file_total_size - send_size
                                data = f.read(size)
                                send_size += len(data)
                            else:
                                data = f.read(1024)
                                send_size += len(data)
                            self.client.send(data)
                            '''
                            打印进度条
                            '''
                            str1 = "已上传 %sByte:" %send_size
                            str2 = '%s%s' % (round((send_size / file_total_size) * 100, 2), '%')
                            str3 = '[%s%s]' % ('*'*i, str2)
                            sys.stdout.write('\033[32;1m\r%s%s\033[0m' % (str1, str3))
                            sys.stdout.flush()
                            i += 2
                            time.sleep(0.3)
                            '''
                            文件加密
                            '''
                            self.m.update(data)
                    self.encryption()
                    '''
                    磁盘配额
                    '''
                    new_disk_quota = round((mesg["disk_quota"]*(2**20) - file_total_size)/(2**20),2)
                    self.user_obj.update_disk_quota(new_disk_quota)
                    print("\033[32;1m磁盘配额还剩：%sM\033[0m"%new_disk_quota)
            else:
                print("\033[31;1m文件不存在\033[0m")

    def encryption(self):
        '''
        文件加密函数
        1、判断用户是否需要加密
        2、取消加密发送'401'信息给服务端
        3、确认加密发送'400'信息给服务端
        4、接收服务端文件加密信息
        5、判断客户端和服务端文件加密信息是否一致
        :return:
        '''
        encryption = input("\n文件已接收是否需要加密认证...按q取消加密>>>")
        if encryption != 'q':
            self.client.send(b'400')
            print('\033[32;1m确认加密\033[0m')
            file_md5 = self.m.hexdigest()
            server_back_md5 = self.client.recv(1024).decode()
            print("\033[32;1m本地文件加密:%s\n服务端文件加密:%s\033[0m" % (file_md5, server_back_md5))
            if file_md5 == server_back_md5:
                print("\033[32;1m加密认证成功\033[0m")
            else:
                print("加密认证失败")
        else:
            self.client.send(b'401')
            print("\033[32;1m\n已取消加密.文件接收成功\033[0m")

    def dir(self,cmd):
        '''
        查看根目录下文件信息函数
        1、dir_home 查看用户本地文件内容
        2、dir_server 查看用户服务器文件内容
        3、接收服务端指令文件大小
        4、发送接收目录信息指令
        5、接收目录信息
        :param cmd:
        :return:
        '''
        if len(cmd) < 2:
            print("\033[31;1m请输入有效指令:\033[0m", self.help_info)
        else:
            if cmd[1] == "home" or cmd[1] == 'server':
                mesg = {
                    "action":cmd[0],
                    "object":cmd[1]
                }
                self.client.send(json.dumps(mesg).encode())
                server_back = self.client.recv(1024).decode()
                print('\033[32;1m收到服务端回调指令大小:\033[0m',server_back)
                self.client.send("ok".encode())
                revered_size = 0
                revered_data = b''
                while revered_size < int(server_back):
                    data = self.client.recv(1024)
                    revered_data += data
                    revered_size = len(data)
                    print('\033[32;1m实际收到指令大小:\033[0m',revered_size)
                else:
                    print(revered_data.decode())
            else:
                print("\033[31;1m请输入有效指令:\033[0m", self.help_info)

    def mkdir(self,cmd):
        '''
        添加目录文件函数
        1、判断指令是否正确
        2、先获取当前路径
        3、判断所添加目录是否已存在
        4、使用os.mkdir()函数添加新目录
        5、新目录添加成功
        :param cmd:
        :return:
        '''
        if len(cmd) < 2:
            print("\033[31;1m请输入有效指令:\033[0m", self.help_info)
        else:
            # file_path = os.path.join(setting.USER_HOME,self.user_path,"user_home",cmd[1])
            file_path = os.path.join(self.pwd_path,cmd[1])
            print("当前路径：", file_path)
            if os.path.exists(file_path):
                print("\033[31;1m该目录文件夹已存在\033[0m")
            else:
                os.mkdir(file_path)
                print("该目录文件夹创建成功")

    def cd(self,cmd):
        '''
        CD:移动到指定目录函数
        1、先判断指令是否正确
        2、判断路径是否有效
        3、根据输入做相应操作如：cd ..:移动到上一级目录   cd / :移动到根目录  cd 目录名:移动到指定目录
        4、拆分路径重新拼接新路径
        5、返回self.pwd_path当前所在目录
        :param cmd:
        :return:
        '''
        if len(cmd) < 2:
            print("\033[31;1m请输入有效指令:\033[0m", self.help_info)
        else:
            if cmd[1] == '..':
                list = []
                pwd_path = os.path.join(self.pwd_path)
                for index in pwd_path.split('\\'):  #列表形式拆分当前目录路径以'\\'分隔
                    list.append(index)          #将目录路径参数添加至list列表中
                list[0] = '%s%s'%(list[0],'/')  #将列表第一个元素 E: 字符串拼接成 E:/
                if list[-1] == "user_home":
                    print("已在根目录下")
                else:
                    del list[-1]    #删除列表最后个元素也就是上一级目录路径
                    self.pwd_path = ''
                    for item in list:       #重新拼接成新的路径
                        self.pwd_path = os.path.join(self.pwd_path,item)
                    print("当前路径：",self.pwd_path)
                    #print(os.listdir(self.pwd_path))
            elif cmd[1] == '/':
                self.pwd_path = os.path.join(setting.USER_HOME,self.user_path,"user_home")
                print("已返回根目录：", self.pwd_path)
            else:
                pwd_path = os.path.join(self.pwd_path,cmd[1])   #移动到指定目录  cmd[1]目录名
                if os.path.isdir(pwd_path):
                    #print(os.listdir(pwd_path))
                    self.pwd_path = pwd_path    #返回用户当前路径
                    print("当前路径：", self.pwd_path)
                else:
                    print("\033[31;1m系统找不到指定的路径\033[0m")

    def pwd(self,cmd):
        '''
        显示当前目录路径
        :param cmd:
        :return:
        '''
        print("当前路径：", self.pwd_path)
        print(os.listdir(self.pwd_path))

    def help(self,cmd):
        '''
        帮助文档函数
        :param cmd:
        :return:
        '''
        print(self.help_info)
