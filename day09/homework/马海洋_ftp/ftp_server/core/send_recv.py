#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/6'

import struct
import json

class Send_recv():
    '''信息发送或接受'''
    def __init__(self,sk):
        self.conn = sk

    def send_file(self, file_path, exist_size, file_total_size):
        '''
        发送文件(download)
        :param file_path: 服务端文件路径
        :param exist_size:  # 客户端已接收大小
        :param file_total_size: # 文件总大小
        '''
        with open(file_path, mode='rb') as f:
            f.seek(exist_size)  # 根据字节数,跳到文件指定位置
            send_size = exist_size  # 已发送字节数
            while send_size < file_total_size:
                data = f.read(8192) # 每次读取8192字节到内存中
                self.conn.send(data)  # 发送内容客户端
                send_size += len(data)  # 已发送字节数加上刚发送的字节数


    def recv_file(self, fileMd5Path, exist_size, upload_size):
        '''
        文件接收(upload)
        :param fileMd5Path: MD5文件路径
        :param exist_size:  已接收文件大小
        :param upload_size:  需要接收的文件总大小
        :return:
        '''
        with open(fileMd5Path, 'ab') as fp: # 以ab形式打开一个文件
            recv_size = exist_size
            while recv_size < upload_size:
                content = self.conn.recv(8192) # 每次接受8192个字节
                fp.write(content)  # 内容写入
                fp.flush() # 内存刷入文件
                recv_size += len(content)

    def send_messages(self,send_dict):
        '''
        发送信息(指令)
        :param send_dict: 发送的字典
        '''
        send_info = json.dumps(send_dict).encode('utf8')
        send_head_lens = struct.pack('i', len(send_info))
        self.conn.send(send_head_lens)
        self.conn.send(send_info)

    def recv_messages(self):
        '''接收信息(指令)'''
        recv_struc = self.conn.recv(4)
        head_num = struct.unpack('i',recv_struc)[0]
        recv_content = self.conn.recv(head_num).decode('utf8')
        recv_json = json.loads(recv_content)
        return recv_json
