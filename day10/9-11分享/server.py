import os
import json
import struct
import hashlib
import socketserver
class Auth:
    @staticmethod
    def get_md5(opt_dic):
        md5 = hashlib.md5(opt_dic['username'].encode('utf-8'))
        md5.update(opt_dic['password'].encode('utf-8'))
        pwd = md5.hexdigest()
        return pwd

    @classmethod
    def login(cls,opt_dic):
        # 把密码按照之前的规则进行加密
        pwd = cls.get_md5(opt_dic)
        # 和文件中的用户名密码进行逐行比对
        with open('userinfo', encoding='utf-8') as f:
            for line in f:
                user, passwd = line.strip().split('|')
                if opt_dic['username'] == user and pwd == passwd:
                    dic = {'operate': 'login', 'flag': True}
                    break
            else:
                dic = {'operate': 'login', 'flag': False}
        return dic

    @classmethod
    def register(cls,opt_dic):
        # 把密码按照自己的算法进行摘要
        pwd = cls.get_md5(opt_dic)
        # 把用户名和密码写在userinfo文件中
        with open('userinfo', 'a', encoding='utf-8') as f:
            f.write('%s|%s\n' % (opt_dic['username'], pwd))
        dic = {'operate': 'register', 'flag': True}
        return dic

class Myserver(socketserver.BaseRequestHandler):
    def mysend(self,dic):
        str_d = json.dumps(dic)
        self.request.send(str_d.encode('utf-8'))

    def myrecv(self,protocol = False,msg_len = 1024):
        if protocol:
            bytes_len = self.request.recv(4)
            msg_len = struct.unpack('i', bytes_len)[0]
        msg = self.request.recv(msg_len)
        str_msg = msg.decode('utf-8')
        opt_dic = json.loads(str_msg)
        return opt_dic

    def handle(self):
        # conn == self.request
        opt_dic = self.myrecv()
        if hasattr(Auth,opt_dic['operate']):
            dic = getattr(Auth,opt_dic['operate'])(opt_dic)
            self.mysend(dic)
        # 判断登录\注册的结果在dic中，如果登录、注册成功，用户上传或者下载
        if dic['flag']:
            opt_dic = self.myrecv(True)
            if opt_dic['operate'] == 'upload':
                # 上传工作
                remote_path = r'E:\python_test\python\day10\9-11分享\remote'
                filename = opt_dic['filename']
                file_path = os.path.join(remote_path,filename)
                with open(file_path,'wb') as f:
                    while opt_dic['filesize']> 0:
                        content = self.request.recv(1024)
                        f.write(content)
                        opt_dic['filesize'] -= len(content)
            elif opt_dic['operate'] == 'download':
                # 下载工作
                print('执行对应的下载逻辑')

#完成反射


sk = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
sk.serve_forever()

