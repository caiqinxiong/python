import re
import os
import sys
import time
import hashlib
from conf import Config

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_file_path = os.path.join(base_dir, "server", "db", "userinfo")
register_log_file_path = os.path.join(base_dir, "server", "log", Config["register_log"])


class Method():
    @staticmethod
    def progress_bar(astep, total_step):
        '''进度条'''
        step_num = int(astep * 100 / total_step)
        if step_num == 100:  # 最后换行
            print("\r%s [%s%%] " % (step_num * ">", step_num))
        else:
            print("\r%s [%s%%] " % (step_num * ">", step_num), end="")
        sys.stdout.flush()

    @staticmethod
    def get_md5(pwd=None, file_size=None, file_path=None):
        if pwd:
            '''md5加密'''
            return hashlib.md5(Config["salt_str"].encode()+pwd.encode()).hexdigest()
        elif file_size:
            '''获取文件内容的md5加密结果'''
            md5_obj = hashlib.md5(Config["salt_str"].encode())
            read_size = 0
            buffer_size = 4096
            with open(file_path, "rb") as f:
                while read_size < file_size:
                    if file_size - read_size <= buffer_size:  # 最后一次发送
                        fcontent = f.read(file_size - read_size)
                    else:  # 非最后一次
                        fcontent = f.read(buffer_size)
                    read_size += len(fcontent)
                    md5_obj.update(fcontent)
            return md5_obj.hexdigest()

    @staticmethod
    def printC(str1, color="black"):
        '''添加颜色输出
        color: red:红色 gre:绿色 yel:黄色
        '''
        col_type = 30
        if color == "red":
            col_type = 31
        elif color == "gre":
            col_type = 32
        elif color == "yel":
            col_type = 33
        print("\033[0;%sm%s\033[0m" % (col_type, str1))

    @staticmethod
    def convert_size(size):
        '''单位换算'''
        size = int(size)
        if size > 1024 * 1024 * 1024:
            size = format(size / 1024 / 1024 / 1024, ".2f") + "GB"
        elif size > 1024 * 1024:
            size = format(size / 1024 / 1024, ".2f") + "MB"
        elif size > 1024:
            size = format(size / 1024, ".2f") + "KB"
        else:
            size = str(size) + "byte"
        return size

    @staticmethod
    def get_user_info(file, field="all"):
        """获取用户列表"""
        lst = []
        if os.path.exists(file):
            with open(file) as f:
                for line in f:
                    try:
                        usr, pwd, quota = line.strip().split("|")
                        if field == "all":
                            lst.append((usr, pwd, quota))
                        else:
                            lst.append(usr)
                    except:
                        break
        return lst

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
