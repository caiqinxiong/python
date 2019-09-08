import os
import json
import time
import struct
import shutil
import shelve
import hashlib
import socketserver

from conf.config import Config

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_file_path = os.path.join(base_dir, "db", "userinfo")
register_log_file_path = os.path.join(base_dir, "log", Config["register_log"])
upload_incomplete_path = os.path.join(base_dir, "upload_incomplete", ".db")
print("upload_incomplete_path", upload_incomplete_path)
shelve_obj = shelve.open(upload_incomplete_path)


class MyServer(socketserver.BaseRequestHandler):
    '''自定义类,继承socketserver.BaseRequestHandler'''

    status_code = {
        100: "Successful register",
        101: "Register failed",
        200: "Successful login",
        201: "Error incorrect username or password",
        300: "Folder creation successful",
        301: "Directory does not exist",
        302: "Folder already exist",
        303: "Folder is not empty",
        304: "File does not exist",
        305: "File already exist",
        400: "Folder delete successful",
        401: "Folder dose not exist",
        402: "It's not a file",
        410: "File delete successful",
        500: "File rename successful",
        501: "New file or folder name already exist",
        600: "Folder rename successful",
        601: "Old file or folder name does not exist",
        602: "File is too big, You don't have enough space",
        700: "File upload successful",
        701: "File upload failed",
        702: "Do not have file to transmission",
    }

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

    def _set_status_code(self, data, code):
        '''设置状态码和状态内容'''
        data["status_code"] = code
        data["status_content"] = self.status_code[code]

    def _mkdir(self, data):
        '''创建文件夹'''
        print("mkdir_data", data)
        dir_path = data["user_path"]
        if os.path.isdir(dir_path):
            mk_dir_path = os.path.join(dir_path, data["choice"][-1])
            if os.path.exists(mk_dir_path):
                self._set_status_code(data, 302)  # 文件夹已存在
            else:
                os.makedirs(mk_dir_path)
                self._set_status_code(data, 300)  # 文件夹创建成功
            self.send_msg(data)

    def _rmdir(self, data):
        '''删除空文件夹'''
        print("rmdir_data", data)
        dir_path = os.path.join(base_dir, "home", data["user"], data["choice"][-1])
        if os.path.isdir(dir_path):
            try:
                os.rmdir(dir_path)
                self._set_status_code(data, 400)  # 文件夹删除成功
            except Exception:
                self._set_status_code(data, 303)  # 文件夹不是空的
        else:
            self._set_status_code(data, 401)  # 文件夹不存在
        self.send_msg(data)

    def _rmtree(self, data):
        '''删除文件夹'''
        print("rm_data", data)
        dir_path = os.path.join(base_dir, "home", data["user"], data["choice"][-1])
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self._set_status_code(data, 400)  # 文件夹删除成功
        else:
            self._set_status_code(data, 401)  # 文件夹不存在
        self.send_msg(data)

    def _remove(self, data):
        '''删除文件'''
        print("remove_data", data)
        file_path = os.path.join(data["user_path"], data["choice"][-1])
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)
                self._set_status_code(data, 410)  # 文件删除成功
            else:
                self._set_status_code(data, 402)  # 他不是文件
        else:
            self._set_status_code(data, 304)  # 文件不存在
        self.send_msg(data)

    def _unlink(self, data):
        '''删除文件'''
        print("unlink_data", data)
        file_path = os.path.join(data["user_path"], data["choice"][-1])
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.unlink(file_path)
                self._set_status_code(data, 410)  # 文件删除成功
            else:
                self._set_status_code(data, 402)  # 他不是文件
        else:
            self._set_status_code(data, 304)  # 文件不存在
        self.send_msg(data)

    def _mv(self, data):
        '''修改文件名'''
        print("mv_data", data)
        old_file_path = os.path.join(data["user_path"], data["choice"][1])
        new_file_path = os.path.join(data["user_path"], data["choice"][-1])
        if os.path.exists(new_file_path):
            self._set_status_code(data, 501)  # 新文件或文件夹已存在
            self.send_msg(data)
        else:
            if os.path.exists(old_file_path):
                if os.path.isdir(old_file_path):
                    self._set_status_code(data, 600)  # 文件名修改成功
                else:
                    self._set_status_code(data, 500)  # 文件名修改成功
                os.rename(old_file_path, new_file_path)
                self.send_msg(data)
            else:
                self._set_status_code(data, 601)  # 旧文件或文件夹不存在
                self.send_msg(data)

    def _cd(self, data):
        '''切换目录
        1. cd /folder 进入家目录下的folder文件夹
        2. cd .. 上一级目录
        3. cd / 家目录
        4. cd folder 进入下一级目录
        5. cd aaaaaaaaaaaa 不存在的目录
        '''
        print("cd_data  server", data)
        data["choice"][-1] = data["choice"][-1].replace("\\", os.sep).replace("/", os.sep)
        if data["choice"][-1].startswith(os.sep) and len(data["choice"][-1]) > 2:  # 1. cd /folder
            data["user_path"] = os.path.join(base_dir, "home", data["user"])  # 3. cd / 进入家目录
            if os.path.isdir(os.path.join(data["user_path"], data["choice"][-1].lstrip(os.sep))):
                data["user_path"] = os.path.join(data["user_path"], data["choice"][-1].lstrip(os.sep))
            else:  # 5. cd aaaaaaaaaaa不存在的目录
                self._set_status_code(data, 301)  # 目录不存在
        elif data["choice"][-1] == os.pardir:  # 2. cd ..
            user_dir = os.path.join(base_dir, "home")
            if os.path.dirname(data["user_path"]) <= user_dir:  # 已经到家目录了
                self._set_status_code(data, 301)  # 目录不存在
            else:  # cd ..返回上级目录
                cd_dir_path = os.path.dirname(data["user_path"])
                data["user_path"] = cd_dir_path
        elif data["choice"][-1] == os.sep:  # 3. cd / 家目录
            data["user_path"] = os.path.join(base_dir, "home", data["user"])
        elif os.path.isdir(os.path.join(data["user_path"], data["choice"][-1])):   # 4. cd folder
            data["user_path"] = os.path.join(data["user_path"], data["choice"][-1])
        else:  # 5. cd aaaaaaaaaaa不存在的目录
            self._set_status_code(data, 301)  # dir 目录不存在
        self.send_msg(data)

    def _touch(self, data):
        '''创建空文件'''
        print("touch_data", data)
        file_path = os.path.join(data["user_path"], data["choice"][-1])
        open(file_path, "w").close()

    def _ls(self, data):
        '''查看文件和文件夹'''
        print("ls_data", data)
        abs_dir = data["user_path"]
        if os.path.isdir(abs_dir):
            data["list_dir"] = os.listdir(abs_dir)
            self.send_msg(data)

    def _used(self, data):
        '''查看用户空间时间情况'''
        print("used_data", data)
        user_path = os.path.join(base_dir, "home", data["user"])
        data["used_size"] = self.get_folder_size(user_path)
        self.send_msg(data)

    def _get(self, data):
        '''下载'''
        print("get_data", data)
        file_path = os.path.join(data["user_path"], data["choice"][-1])  # 下载文件路径
        if os.path.exists(file_path) and os.path.isfile(file_path):
            file_size = os.stat(file_path).st_size  # 文件大小
            data["file_size"] = file_size  # 保存到data字典中
            self.send_msg(data)
            send_size = 0
            md5_obj = hashlib.md5()  # 创建md5对象
            with open(file_path, "rb") as f:
                while send_size < file_size:  # 循环发送
                    if file_size - send_size < Config["buffer_size"]:  # 最后一次发送
                        fcontent = f.read(file_size - send_size)
                    else:  # 非最后一次
                        fcontent = f.read(Config["buffer_size"])
                    self.request.send(fcontent)
                    send_size += len(fcontent)
                    md5_obj.update(fcontent)  # 文件内容做md5加密
            server_file_md5 = md5_obj.hexdigest()  # 服务端文件内容加密结果
            data["server_file_md5"] = server_file_md5  # 保存到data字典中
        else:
            self._set_status_code(data, 304)  # 文件不存在
        self.send_msg(data)

    def _reget(self, data):
        '''未下载完的文件,继续下载'''
        print("reget_data1", data)
        file_size = data["file_size"]  # 文件大小
        temp_file_size = data["temp_file_size"]  # 临时文件大小
        file_path = os.path.join(data["user_path"], data["choice"][-1])
        send_size = temp_file_size  # 发送数据的开始位置
        with open(file_path, "rb") as f:  # 读取文件,文件可能是视频登录
            f.seek(send_size)  # 发送数据的开始位置
            while send_size < file_size:  # 循环发送
                if file_size - send_size < Config["buffer_size"]:  # 最后一次发送
                    fcontent = f.read(file_size - send_size)
                else:  # 非最后一次
                    fcontent = f.read(Config["buffer_size"])
                self.request.send(fcontent)
                send_size += len(fcontent)
        server_file_md5 = self._get_md5(file_size=file_size, file_path=file_path)  # 服务端文件内容加密结果
        data["server_file_md5"] = server_file_md5  # 保存到字典
        self.send_msg(data)

    def _put(self, data):
        '''上传文件'''
        print("put_data", data)
        file_name = data["file_name"]  # 文件名
        file_path = os.path.join(data["user_path"], file_name)  # 上传文件存放的文件名
        if os.path.exists(file_path):  # 文件名已存在
            self._set_status_code(data, 305)
            self.send_msg(data)
        else:
            user_path = os.path.join(base_dir, "home", data["user"])
            file_size = data["file_size"]
            total_size = self.get_folder_size(user_path) + file_size
            if int(data["quota"]) < total_size:  # 空间不足
                self._set_status_code(data, 602)
                self.send_msg(data)
            else:
                self.send_msg(data)
                recv_size = 0
                md5_obj = hashlib.md5()
                temp_file_name = "%s.tmp" % time.time()  # 临时文件名
                temp_file_path = os.path.join(base_dir, "upload", temp_file_name)  # 临时文件绝对值路径
                data["temp_file_name"] = temp_file_name  # 保存临时文件名
                data["temp_file_path"] = temp_file_path
                data["action_type"] = "reput"
                global shelve_obj  # 定义在初始化方法里,有问题,最后就定义在了类外面^-^
                shelve_obj[temp_file_name] = data  # 临时文件名作为键值保存
                with open(temp_file_path, "ab") as f:
                    while recv_size < file_size:  # 循环写文件内容
                        if file_size - recv_size < Config["buffer_size"]:  # 最后一次接收
                            fcontent = self.request.recv(file_size - recv_size)
                        else:
                            fcontent = self.request.recv(Config["buffer_size"])  # 非最后一次接收
                        recv_size += len(fcontent)  # 更新已接收文件大小
                        f.write(fcontent)
                        md5_obj.update(fcontent)
                server_file_md5 = md5_obj.hexdigest()  # 服务端文件内容md5加密结果
                up_data = self.recv_msg()  # 接收服务端字典
                if up_data["client_file_md5"] == server_file_md5:  # 客户端和服务端文件内容一致
                    if shelve_obj[temp_file_name]:
                        del shelve_obj[temp_file_name]
                    os.rename(temp_file_path, file_path)  # 将临时文件名改为真实文件名
                    up_data["used_size"] = total_size  # 更新用户空间已使用情况
                    self._set_status_code(up_data, 700)  # 更新状态码
                    self.send_msg(up_data)
                else:
                    self._set_status_code(up_data, 701)  # 文件内容不一致
                    self.send_msg(up_data)

    def _reput(self, data):
        '''未上传完的文件,继续上传'''
        print("reput_data1", data)
        file_size = data["file_size"]
        temp_file_path = data["temp_file_path"]
        temp_file_name = data["temp_file_name"]
        file_path = os.path.join(data["user_path"], data["choice"][-1])
        temp_file_size = os.stat(temp_file_path).st_size
        data["temp_file_size"] = temp_file_size
        self.send_msg(data)
        recv_size = temp_file_size  # 已发送大小等于临时文件大小
        with open(temp_file_path, "ab") as f:  # 追加写入临时文件
            f.seek(recv_size)  # 移动文件写指针到文件最后位置
            while recv_size < file_size:  # 循环写
                if file_size - recv_size < Config["buffer_size"]:  # 最后一次接收
                    fcontent = self.request.recv(file_size - recv_size)
                else:  # 非最后一次接收
                    fcontent = self.request.recv(Config["buffer_size"])
                recv_size += len(fcontent)
                f.write(fcontent)
        server_file_md5 = self._get_md5(file_size=file_size, file_path=temp_file_path)  # 客户端文件内容md5加密结果
        reput_data = self.recv_msg()
        if reput_data["client_file_md5"] == server_file_md5:  # 对比服务端和客户端文件内容是否一致
            os.rename(temp_file_path, file_path)  # 将临时文件名改为真实文件名
            global shelve_obj
            if shelve_obj[temp_file_name]:
                del shelve_obj[temp_file_name]  # 文件下载完,就删除文件中字典的key
            self._set_status_code(reput_data, 700)
        else:
            self._set_status_code(reput_data, 701)
        self.send_msg(reput_data)

    def _put_incomplete(self, data):
        '''查看未完成的上传文件,断点续传'''
        print("put_incomplete", data)
        global shelve_obj
        for k, v in enumerate(list(shelve_obj), 1):
            print(k, v, shelve_obj[v])
        if list(shelve_obj.keys()):  # 所有未上传完的文件
            incomplete_dic = {}
            for k, v in enumerate(list(shelve_obj), 1):
                # 该用户未上传完的文件
                if shelve_obj[v]["user"] == data["user"] and shelve_obj[v]["action_type"] == "reput":
                    incomplete_dic[v] = shelve_obj[v]
            data["incomplete_dic"] = incomplete_dic
        self.send_msg(data)

    def _login(self, data):
        '''登录'''
        with open(db_file_path, "r", encoding="utf-8") as f:
            for line in f:
                u_lst = line.strip().split("|")
                if data["user"] == u_lst[0] and data["pwd"] == u_lst[1]:  # 登录成功
                    self._set_status_code(data, 200)
                    data["user_path"] = os.path.join(base_dir, "home", data["user"])
                    data["user_dir"] = os.path.join(base_dir, "home")
                    data["used_size"] = self.get_folder_size(data["user_path"])
                    data["quota"] = u_lst[-1]
                    self.send_msg(data)
                    break
            else:  # 登录失败
                self._set_status_code(data, 201)  # 用户名或密码错误
                self.send_msg(data)

    def _register(self, data):
        '''注册'''
        print("register_data", data)
        self.write_log(db_file_path, "%s|%s|%s\n" % (data["user"], data["pwd"], data["quota"]), 1)
        self.write_log(register_log_file_path, "User [%s] login successful.\n" % data["user"])
        self._set_status_code(data, 100)
        data["user_path"] = os.path.join(base_dir, "home", data["user"])
        if not os.path.exists(data["user_path"]):
            os.makedirs(data["user_path"])
        data["user_dir"] = os.path.join(base_dir, "home")
        data["used_size"] = 0
        self.send_msg(data)

    def handle(self):
        '''必须有的方法'''
        while 1:
            try:
                data_msg = self.recv_msg()
                if hasattr(self, "_%s" % data_msg["action_type"]):  # 反射
                    getattr(self, "_%s" % data_msg["action_type"])(data_msg)
            except Exception:
                break

    @staticmethod
    def get_folder_size(path):
        '''计算某路径下所有文件和文件夹的总大小'''
        total_size = 0
        for root, folder_lst, file_lst in os.walk(path):
            for file in file_lst:
                total_size += os.stat(os.path.join(root, file)).st_size
        return total_size

    @staticmethod
    def _get_md5(file_size, file_path):
        '''获取文件内容的md5'''
        md5_obj = hashlib.md5(Config["salt_str"].encode())
        read_size = 0
        with open(file_path, "rb") as f:
            while read_size < file_size:
                if file_size - read_size <= Config["buffer_size"]:  # 最后一次发送
                    fcontent = f.read(file_size - read_size)
                else:  # 非最后一次
                    fcontent = f.read(Config["buffer_size"])
                read_size += len(fcontent)
                md5_obj.update(fcontent)
        return md5_obj.hexdigest()

    @staticmethod
    def isdir_exists(file):
        """判断目录是否存在,不存在直接创建"""
        folder = os.path.dirname(file)
        if not os.path.exists(folder):
            os.makedirs(folder)

    def write_log(self, file, content, flag=0):
        """
        写日志
        :param file: 日志文件名
        :param content: 日志内容
        """
        self.isdir_exists(file)
        mode = "w"  # 默认为新建
        if os.path.exists(file):
            mode = "a"  # 存在则追加

        with open(file, mode, encoding="utf-8") as f:
            if flag:
                f.write(content)
            else:
                f.write(time.strftime("%Y-%m-%d %X ") + content)
