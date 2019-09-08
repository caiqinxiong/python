import os
import re
import sys
import json
import time
import struct
import socket
import shelve
import hashlib

from method import Method
from conf import Config
base_dir = os.path.dirname(os.path.abspath(__file__))
gran_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_file_path = os.path.join(gran_dir, "server", "db", "userinfo")


class Client(Method):
    reg_opera_lst = [
        ("login", "登录"),
        ("register", "注册"),
    ]
    operate_lst = [
        ("mkdir", "创建文件夹"),
        ("rmdir", "删除空文件夹"),
        ("rmtree", "删除文件夹"),
        ("remove", "删除文件"),
        ("unlink", "删除文件"),
        ("mv", "修改文件(夹)名"),
        ("touch", "新建文件"),
        ("cd", "切换目录"),
        ("ls", "查看当前目录下的文件和文件夹"),
        ("get", "下载"),
        ("get_incomplete", "未完成下载的文件"),
        ("put", "上传"),
        ("put_incomplete", "未完成上传的文件"),
        ("used", "查看用户空间配额使用情况"),
        ("pwd", "查看当前目录"),
        ("help", "帮助"),
        ("bye", "退出程序"),
   ]

    '''客户端类,继承Methond类'''
    def __init__(self):
        self.host = Config["server_ip"]
        self.port = Config["server_port"]
        self.buffer_size = Config["buffer_size"]
        self.shelve_obj = shelve.open(os.path.join(base_dir, "download_incomplete", ".db"))

    def invalid_command(self):
        '''无效的命令'''
        self.printC("Invalid command, help", "red")

    def _write_file(self, file_path, file_size, mode="ab"):
        '''文件写操作, 返回文件内容md5加密结果'''
        md5_obj = hashlib.md5()  # 创建md5对象
        recv_size = 0  # 已接收默认为0
        with open(file_path, mode) as f:  # 追加写文件
            while recv_size < file_size:  # 循环接收
                if file_size - recv_size < self.buffer_size:  # 最后一次接收
                    fcontent = self.request.recv(file_size - recv_size)
                else:  # 非最后一次接收
                    fcontent = self.request.recv(self.buffer_size)
                recv_size += len(fcontent)  # 已接收变量自增
                f.write(fcontent)
                self.progress_bar(recv_size, file_size)  # 显示下载进度条
                md5_obj.update(fcontent)  # 将每次接收到的数据追加到md5中
        return md5_obj.hexdigest()  # 客户端下载文件内容md5值

    def _rewrite_file(self, file_path, temp_file_size, file_size, mode="ab"):
        '''文件重新操作'''
        recv_size = temp_file_size  # 已发送大小等于临时文件大小
        with open(file_path, mode) as f:  # 追加写入临时文件
            f.seek(recv_size)  # 移动文件写指针到文件最后位置
            while recv_size < file_size:  # 循环写
                if file_size - recv_size < Config["buffer_size"]:  # 最后一次接收
                    fcontent = self.request.recv(file_size - recv_size)
                else:  # 非最后一次接收
                    fcontent = self.request.recv(Config["buffer_size"])
                recv_size += len(fcontent)
                f.write(fcontent)
                self.progress_bar(recv_size, file_size)  # 显示下载进度条

    def _read_file(self, file_path, file_size, mode="rb"):
        '''文件读操作,返回文件内容md5加密结果'''
        md5_obj = hashlib.md5()
        send_size = 0
        with open(file_path, mode) as f:
            while send_size < file_size:  # 循环读取文件
                if file_size - send_size < self.buffer_size:  # 最后一次读取
                    fcontent = f.read(file_size - send_size)
                else:
                    fcontent = f.read(self.buffer_size)  # 非最后一次读取
                self.request.send(fcontent)  # 发送给服务端
                send_size += len(fcontent)  # 已发送文件大小
                md5_obj.update(fcontent)  # 逐渐加密文件内容
                self.progress_bar(send_size, file_size)  # 显示上传进度条
        return md5_obj.hexdigest()  # 客户端文件内容加密结果

    def recv_msg(self):
        '''接收消息
        [第一次接收的数据长度]长度为4(bytes)-->struct.unpack解包,元组,取第一个元素,数据长度(int)
        -->接收定长数据[第二接收的数据长度]-->解码(decode)-->反序列化json.loads(dict)
        '''
        head_size = self.request.recv(4)
        head_data_len = struct.unpack('i', head_size)[0]
        head_data = self.request.recv(head_data_len).decode()
        return json.loads(head_data)

    def send_msg(self, data):
        '''发送消息
        :param data:dict字典类型的数据
        dict(字典)-->json.dumps(序列化字符串)-->encode编码(bytes)[第二次发送的数据]
        -->len数据长度(int)-->struct.pack打包(定长的bytes)[第一次发送的数据]
        '''
        head_data = json.dumps(data).encode()
        head_size = struct.pack('i', len(head_data))
        self.request.send(head_size)
        self.request.send(head_data)

    def _send_msg_action(self, data):
        '''发送消息前,重置action_type'''
        data["action_type"] = data["choice"][0]
        self.send_msg(data)

    def _msg_judge(self, data, code, code2=None):
        if data.get("status_code") == code or data.get("status_code") == code2:
            self.printC(data.get("status_content"), "gre")
        else:
            self.printC(data.get("status_content"), "red")

    def _recv_msg_judge(self, data, code, code2=None):
        '''接收消息,根据状态码做判断'''
        self._send_msg_action(data)
        new_data = self.recv_msg()
        self._msg_judge(new_data, code, code2)

    def _mkdir(self, data):
        '''创建文件夹'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 300)

    def _rmdir(self, data):
        '''删除空文件夹'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 400)

    def _rmtree(self, data):
        '''删除文件夹'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 400)

    def _remove(self, data):
        '''删除文件'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 410)

    def _unlink(self, data):
        '''删除文件'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 410)

    def _mv(self, data):
        '''修改文件名'''
        if len(data["choice"]) != 3:
            self.invalid_command()
        else:
            self._recv_msg_judge(data, 500, code2=600)

    def _cd(self, data):
        '''切换目录'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            data["action_type"] = data["choice"][0]
            if len(data["choice"]) <= 1:
                self.printC("invalid command", "red")
            else:
                self.send_msg(data)
                data = self.recv_msg()
                if data.get("status_code") == 301:
                    self.printC(data.get("status_content"), "red")
                else:
                    self.handle(data)

    def _touch(self, data):
        '''创建空文件'''
        if len(data["choice"]) != 2:
            self.invalid_command()
        else:
            self._send_msg_action(data)

    def _ls(self, data):
        '''查看当前目录下的文件和文件夹'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            self._send_msg_action(data)
            ls_data = self.recv_msg()
            if ls_data.get("list_dir"):  # 目录列表
                for f in ls_data.get("list_dir"):  # 遍历目录列表
                    file_path = os.path.join(data["user_path"], f)  # 文件路径
                    filesize = self.convert_size(os.stat(file_path).st_size)  # 文件大小
                    filectime = time.strftime("%Y-%m-%d %X", time.localtime(os.path.getmtime(file_path)))  # 文件最后修改时间
                    if os.path.isdir(file_path):  # 如果是文件夹
                        self.printC("%s %s <DIR> %s" % (filectime, filesize, f), "gre")
                    else:  # 如果是文件
                        self.printC("%s %s <FILE> %s" % (filectime, filesize, f), "gre")

    def _pwd(self, data):
        '''查看当前目录'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            self.printC(data["user_path"].replace(data["user_dir"], ""), "gre")

    def _used(self, data):
        '''空间已使用大小'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            self._send_msg_action(data)
            data = self.recv_msg()
            self.printC("Total quota: %s" % self.convert_size(data["quota"]), "gre")
            self.printC("Used size: %s" % self.convert_size(data["used_size"]), "red")

    def _help(self, data=None):
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            for meth, operate in self.operate_lst:  # 显示登录和注册功能
                self.printC("%s %s" % (meth, operate), "yel")

    def _bye(self, data):
        '''退出程序'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            self.shelve_obj.close()
            sys.exit("退出程序.")

    def _get(self, data):
        '''下载文件'''
        file_path = os.path.join(base_dir, "download", data["choice"][-1])  # 下载的文件路径
        if os.path.exists(file_path):  # 判断客户端是否已经有该文件
            self.printC("[%s] already exists." % data["choice"][-1], "red")
            self.handle(data)
        else:
            if len(data["choice"]) != 2:
                self.invalid_command()  # 命令无效
            else:
                self._send_msg_action(data)
                get_data = self.recv_msg()
                if get_data.get("file_size"):
                    file_size = get_data.get("file_size")  # 文件大小
                    temp_file_name = "download/%s.temp" % time.time()  # 临时文件名
                    get_data["temp_file_name"] = temp_file_name  # 临时文件名保存到字典
                    get_data["action_type"] = "reget"
                    self.shelve_obj[temp_file_name] = get_data  # 将字典保存到文件中
                    client_file_md5 = self._write_file(temp_file_name, file_size)  # 文件读写操作
                    get_data_dict = self.recv_msg()
                    if get_data_dict["server_file_md5"] == client_file_md5:  # 对比服务端和客户端文件内容是否一致
                        os.rename(temp_file_name, "download/%s" % get_data_dict["choice"][-1])  # 将临时文件名修改为真实文件名
                        del self.shelve_obj[temp_file_name]  # 文件下载完,就删除文件中字典的key
                        self.printC("[%s] download successful." % get_data_dict["choice"][-1], "gre")
                    else:
                        self.printC("[%s] is difference of client and server." % get_data_dict["choice"][-1], "red")
                elif get_data.get("status_code") == 304:
                    self.printC(get_data.get("status_content"), "red")

    def _get_incomplete(self, data):
        '''查看未完成的下载文件,断点续传'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            while 1:
                if list(self.shelve_obj.keys()):  # 所有未下载完的文件
                    incomplete_dic = {}
                    for k, v in enumerate(list(self.shelve_obj), 1):
                        # 该用户未下载完的文件
                        if self.shelve_obj[v]["user"] == data["user"] and self.shelve_obj[v]["action_type"] == "reget":
                            incomplete_dic[v] = self.shelve_obj[v]
                    if incomplete_dic:
                        for k, v in enumerate(incomplete_dic, 1):
                            print(k, self.shelve_obj[v]["choice"][-1])
                        inp = input("请输入您要继续下载的序号: ").strip()
                        if not inp:continue  # 判断是否为空
                        if inp.upper() == "Q":break  # 直接退出
                        if inp.isdigit():  # 输入的是否为数字
                            inp = int(inp)
                            if 1 <= inp <= k:  # 输入是否是正确的序号
                                sel_file_name = list(self.shelve_obj.keys())[inp - 1]  # 文件中的键值
                                if hasattr(self, "_%s" % self.shelve_obj[sel_file_name]["action_type"]):  # 反射
                                    getattr(self, "_%s" % self.shelve_obj[sel_file_name]["action_type"])(sel_file_name)
                            else:
                                self.printC("序号不存在.", "red")
                        else:
                            self.printC("序号不存在.", "red")
                    else:
                        self.printC("没有继续要传输的文件.", "red")
                        break
                else:
                    self.printC("没有未完成下载的文件.", "red")
                    break

    def _reget(self, temp_fname):
        '''未下载完的文件,继续下载'''
        reget_data = self.shelve_obj[temp_fname]  # 数据字典
        temp_file_name = reget_data["temp_file_name"]  # 临时文件名
        temp_file_size = os.stat(temp_file_name).st_size  # 临时文件大小
        file_size = reget_data["file_size"]  # 文件大小
        reget_data["temp_file_size"] = temp_file_size  # 将临时文件大小保存到字典中
        self.send_msg(reget_data)  # 发送给服务端
        self._rewrite_file(temp_file_name, temp_file_size, file_size)  # 文件重写操作
        client_file_md5 = self.get_md5(file_size=file_size, file_path=temp_file_name)  # 客户端文件内容md5加密结果
        get_data = self.recv_msg()
        if get_data["server_file_md5"] == client_file_md5:  # 对比服务端和客户端文件内容是否一致
            os.rename(temp_file_name, "download/%s" % get_data["choice"][-1])  # 将临时文件名改为真实文件名
            del self.shelve_obj[temp_fname]  # 文件下载完,就删除文件中字典的key
            self.printC("[%s] download successful." % get_data["choice"][-1], "gre")  # 显示文件下载成功
            self.handle(get_data)

    def _put(self, data):
        '''上传文件'''
        if len(data["choice"]) != 2:
            self.invalid_command()  # 无效的命令
        else:
            file_path = os.path.join(base_dir, "upload", data["choice"][-1])  # 上传文件的路径
            if os.path.exists(file_path) and os.path.isfile(file_path):  # 存在,并是文件
                data["file_name"] = data["choice"][-1]  # 文件名
                file_size = os.stat(file_path).st_size  # 文件大小
                data["file_size"] = file_size  # 保存文件大小
                self._send_msg_action(data)  # 修改action_type并发送给服务端
                up_data = self.recv_msg()  # 接收服务端的消息
                if up_data:
                    # 文件已存在或空间不足
                    if up_data["status_code"] == 305 or up_data["status_code"] == 602:
                        self._msg_judge(up_data, 700)
                    else:
                        up_data["client_file_md5"] = self._read_file(file_path, file_size)  # 文件读操作
                        self.send_msg(up_data)  # 将字典发送给服务端
                        up_data_dict = self.recv_msg()  # 接收来自服务端的字典
                        if up_data_dict["status_code"] == 700:
                            self.printC("[%s] upload successful." % up_data_dict["choice"][-1], "gre")
                        elif up_data_dict["status_code"] == 701:
                            self.printC("[%s] is difference of client and server." % up_data_dict["choice"][-1], "red")
            else:
                self.printC("文件不存在.", "red")

    def _reput(self, data):
        '''未上传完的文件,继续上传'''
        self.send_msg(data)
        file_size = data["file_size"]  # 文件大小
        reput_data = self.recv_msg()
        temp_file_size = reput_data.get("temp_file_size")
        file_path = os.path.join(base_dir, "upload", data["choice"][-1])
        send_size = temp_file_size  # 发送数据的开始位置
        with open(file_path, "rb") as f:  # 读取文件,文件可能是视频登录
            f.seek(send_size)  # 发送数据的开始位置
            while send_size < file_size:  # 循环发送
                if file_size - send_size < self.buffer_size:  # 最后一次发送
                    fcontent = f.read(file_size - send_size)
                else:  # 非最后一次
                    fcontent = f.read(self.buffer_size)
                self.request.send(fcontent)
                send_size += len(fcontent)
                self.progress_bar(send_size, file_size)
        client_file_md5 = self.get_md5(file_size=file_size, file_path=file_path)  # 服务端文件内容加密结果
        reput_data["client_file_md5"] = client_file_md5  # 保存到字典
        self.send_msg(reput_data)
        reput_code_data = self.recv_msg()
        if reput_code_data["status_code"] == 700:
            self.printC("[%s] upload successful." % reput_code_data["choice"][-1], "gre")  # 显示文件下载成功
            self.handle(reput_code_data)
        else:
            self.printC("[%s] upload failed." % reput_code_data["choice"][-1], "red")

    def _put_incomplete(self, data):
        '''查看未完成的上传文件,断点续传'''
        if len(data["choice"]) != 1:
            self.invalid_command()
        else:
            self._send_msg_action(data)
            put_data = self.recv_msg()
            if put_data.get("incomplete_dic"):
                incomplete_dict = put_data["incomplete_dic"]
                if incomplete_dict:
                    incomplete_lst = []
                    for k, v in enumerate(incomplete_dict, 1):
                        incomplete_lst.append((v, incomplete_dict[v]))
                    while 1:
                        for n, (temp_file, dic) in enumerate(incomplete_lst, 1):
                            print(n, dic["choice"][-1])
                        inp = input("请输入您要继续上传序号: ").strip()
                        if not inp: continue  # 判断是否为空
                        if inp.upper() == "Q": break  # 直接退出
                        if inp.isdigit():  # 输入的是否为数字
                            inp = int(inp)
                            if 1 <= inp <= n:  # 输入是否是正确的序号
                                sel_file_name = incomplete_lst[inp - 1][0]  # 文件中的键值
                                if hasattr(self, "_%s" % incomplete_dict[sel_file_name]["action_type"]):  # 反射
                                    getattr(self, "_%s" % incomplete_dict[sel_file_name]["action_type"])(incomplete_lst[inp - 1][1])
                            else:
                                self.printC("序号不存在.", "red")
                        else:
                            self.printC("序号不存在.", "red")
            else:
                self.printC("没有未完成上传的文件.", "red")


    def handle(self, data):
        '''解析指令并交给具体的方法处理'''
        while 1:
            user_path = data["user_path"].replace(data["user_dir"], "")
            choice = input("[%s@%s]$ " % (data["user"], user_path)).strip().split()
            if not choice:continue
            data['choice'] = choice
            if hasattr(self, "_%s" % choice[0]):  # 发射
                getattr(self, "_%s" % choice[0])(data)  # 执行方法
            else:
                self.printC("Invalid command, help", "red")

    def connect_socket(self):
        '''创建socket套接字'''
        self.request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.request.connect((self.host, self.port))

    def _login(self):
        '''登录'''
        while 1:
            usr = input("Login Username: ").strip().lower()
            if usr == "":  # 判断用户名是否为空
                self.printC("Username cannot be empty.", "red")
                continue
            if usr.upper() == "Q":  # 用户输入q退出该功能
                self.printC("Exit login Function.", "red")
                break
            pwd = input("Login Password: ").strip()
            if pwd == "":  # 判断密码是否为空
                self.printC("Password cannot be empty.", "red")
                continue
            if pwd.upper() == "Q":  # 用户输入q退出该功能
                self.printC("Exit login Function.", "red")
                break
            data = {
                "user": usr,
                "pwd": self.get_md5(pwd),
                "action_type": "login",
            }
            self.send_msg(data)
            login_data = self.recv_msg()
            if login_data.get("status_code") == 200:  # 登录成功
                self.printC(login_data.get("status_content"), "gre")
                self.handle(login_data)
            elif login_data.get("status_code") == 201:  # 登录失败
                self.printC(login_data.get("status_content"), "red")

    def _register(self):
        """注册"""
        while 1:
            usr = input("Register Username: ").strip().lower()
            if usr == "":  # 判断用户名是否为空
                self.printC("Username cannot be empty.", "red")
                continue
            if usr.upper() == "Q":  # 用户输入q退出该功能
                self.printC("Exit register Function.", "red")
                break
            if len(usr) < 4:  # 用户名长度必须大于4
                self.printC("Username length should not be less than 4.", "red")
                continue
            if usr in self.get_user_info(db_file_path, "usr"):  # 判断用户名是否已存在,用户列表[usr1,usr2,...]
                self.printC("Username already exists.", "red")
                continue
            pwd = input("Register Password: ").strip()
            if pwd == "":  # 判断密码是否为空
                self.printC("Password cannot be empty.", "red")
                continue
            if pwd.upper() == "Q":  # 用户输入q退出该功能
                self.printC("Exit register Function.", "red")
                break
            if len(pwd) < 8 or len(pwd) > 20:  # 判断密码的长度是否在8~20之间
                self.printC("Password length must be 8-20 bits.", "red")
                continue
            if re.match(r"[0-9]{8,}", pwd):  # 判断密码是否为纯数字
                self.printC("Password cannot be a pure number.", "red")
                continue
            if re.match(r"[a-zA-Z]{8,}", pwd):  # 判断密码是否为纯字母
                self.printC("Passwords cannot be pure letters.", "red")
                continue
            quota = input("Maximum user space size, default 500(M): ").strip()  # 用户空间配额
            if quota.upper() == "Q":  # 用户输入q退出该功能
                self.printC("Exit register Function.", "red")
                break
            if quota == "":  # 判断用户空间配额是否为空,为空,默认为500M
                quota = 500*1024*1024
            elif quota.isdigit():
                quota = int(quota)*1024*1024
            else:
                self.printC("Quotas must be a number.", "red")
                continue
            data = {
                "user": usr,
                "pwd": self.get_md5(pwd),
                "quota": quota,
                "action_type": "register",
            }
            self.send_msg(data)
            reg_data = self.recv_msg()
            if reg_data.get("status_code") == 100:  # 注册成功
                self.printC(reg_data.get("status_content"), "gre")
                self.handle(reg_data)

def welcome(client):
    """入口欢迎信息"""
    client.printC("Welcome to FTP System".center(50, "*"), "gre")
    while 1:
        for num, (meth, operate) in enumerate(client.reg_opera_lst, 1):  # 显示登录和注册功能
            client.printC("%s %s %s" % (num, meth, operate), "yel")
        inp = input("Select Operation serial number: ").strip()
        if inp.isdigit():  # 判断输入的是否为数字
            inp = int(inp)
            if inp > num or inp <= 0:  # 判断输入的序号是否存在
                client.printC("No serial number exists.", "red")
                continue
            else:
                if hasattr(client, "_%s" % client.reg_opera_lst[inp - 1][0]):  # 判断对象内是否有xxx属性
                    getattr(client, "_%s" % client.reg_opera_lst[inp - 1][0])()  # 获取对象中的xxx属性
        else:
            if inp.upper() == "Q":  # 用户输入q或者Q则退出
                exit("Exit.")
            client.printC("No serial number exists.", "red")
            continue


if __name__ == '__main__':
    """入口程序"""
    client = Client()
    client.connect_socket()
    welcome(client)