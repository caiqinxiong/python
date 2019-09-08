#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/4'

import struct
import hashlib
import json
import sys

class Combination():

    def __init__(self,sk):
        '''
        初始化函数
        :param sk: socket连接对象
        '''
        self.conn = sk

    def file_get_md5(self,file):
        '''
        文件MD5生成
        :param file: 文件路径
        :return: 返回文件生成后的md5
        '''
        md5 = hashlib.md5()
        with open(file, mode='rb') as fp:
            # 按行读取
            for line in fp:
                md5.update(line) # 计算更新MD5
        return md5.hexdigest() # 文件总MD5值

    def processBar(self,num, total):
        '''
        进度条功能
        :param num: 当前大小
        :param total:  文件总大小
        :return:
        '''
        rate = num / total
        rate_num = int(rate * 100)
        if rate_num == 100:
            r = '\r%s>%d%%\n' % ('*' * rate_num, rate_num,)
        else:
            r = '\r%s>%d%%' % ('*' * rate_num, rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush

    def send_messages(self,send_dict):
        '''
        发送信息(指令)
        :param send_dict: 命令信息字典
        :return:
        '''
        send_info = json.dumps(send_dict).encode('utf8') # 序列化后编码
        send_head_lens = struct.pack('i', len(send_info)) # 计算字节数打包为4个字符
        self.conn.send(send_head_lens)  # 发送头部信息
        self.conn.send(send_info)  # 发送内容

    def recv_messages(self):
        '''
        接受信息
        :return: 返回一个信息字典
        '''
        recv_struc = self.conn.recv(4)  # 收4个字符
        head_num = struct.unpack('i',recv_struc)[0]  # 解包
        recv_content = self.conn.recv(head_num).decode('utf8')  # 自定义协议，接受struct解包后的内容字节数
        recv_json = json.loads(recv_content)  # 反序列化
        return recv_json

    def send_file(self,file_path,exist_size, file_total_size):
        '''
        文件传输(upload)
        :param file_path: 文件本地存放路径
        :param exist_size:  服务段当前文件大小
        :param file_total_size:  文件总大小
        :return:
        '''
        # 打开要上传的文件
        with open(file_path, mode='rb') as f:
            # 根据输入的当前字节数 跳到对应的位置
            f.seek(exist_size)
            send_size = exist_size
            # 当前大小小于总大小
            while send_size < file_total_size:
                # 每次读取8192字节
                data = f.read(8192)
                # 发送给服务端
                self.conn.sendall(data)
                # 当前大小+上发过去的字节数量
                send_size += len(data)
                # 打印进度条
                self.processBar(send_size, file_total_size)

    def recv_file(self,file_md5_path,exist_size,download_size):
        '''
        文件接受(download)
        :param file_md5_path: 本地md5路径
        :param exist_size: 本地当前大小
        :param download_size: 要下载的总大小
        :return:
        '''
        # 打开一个MD5的名称路径文件
        with open(file_md5_path, 'ab') as fp:
            # 当前文件大小
            recv_size = exist_size
            # 当前文件大小小于下载总大小
            while recv_size < download_size:
                # 每次接受8192字节数
                content = self.conn.recv(8192)
                # 写入内存
                fp.write(content)
                # 刷到文件中，释放掉内存中的数据
                fp.flush()
                # 当前字节 + 上已写入文件的字节数字
                recv_size += len(content)
                self.processBar(recv_size, download_size)

    def quit(self):
        '''程序结束'''
        cmd_dict = {'cmd': 'quit'}
        self.send_messages(cmd_dict) # 发送指令到服务端
        self.conn.close() # 然后断开连接
        exit()  # 程序退出