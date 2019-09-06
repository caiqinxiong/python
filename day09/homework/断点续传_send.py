# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:13
import socket
import struct
import sys
import os
import time

if __name__ == '__main__':

    file_name = sys.argv[1]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostname(), 12345))

    # 定义文件头信息；
    file_head = struct.pack('128sl', os.path.basename(file_name).encode(),
                        os.stat(file_name).st_size)

    sock.send(file_head)

    received_size = int(sock.recv(2014).decode())

    read_file = open(file_name, "rb")
    read_file.seek(received_size)
    while True:
        # time.sleep(1)
        file_data = read_file.read(10240)

        if not file_data:
            break

        sock.send(file_data)

    read_file.close()
    sock.close()
