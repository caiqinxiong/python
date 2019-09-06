# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/6 17:14

import socket
import threading
import os
import struct


def sending_file(connection):
    try:
        file_info_size = struct.calcsize('128sl')

        buf = connection.recv(file_info_size)

        if buf:
            file_name, file_size = struct.unpack('128sl', buf)
            file_name = file_name.decode().strip('\00')

            file_new_dir = os.path.join('receive')
            # print(file_name, file_new_dir)
            if not os.path.exists(file_new_dir):
                os.makedirs(file_new_dir)

            file_new_name = os.path.join(file_new_dir, file_name)

            received_size = 0
            if os.path.exists(file_new_name):
                received_size = os.path.getsize(file_new_name)

            connection.send(str(received_size).encode())

            w_file = open(file_new_name, 'ab')

            print("start receiving file:", file_name)

            while not received_size == file_size:

                r_data = connection.recv(10240)
                received_size += len(r_data)
                w_file.write(r_data)

            w_file.close()

            print("接收完成！\n")

        connection.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    host = socket.gethostname()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, 12345))
    sock.listen(5)

    print("服务已启动---------------")

    while True:
        connection, address = sock.accept()
        print("接收地址：", address)
        thread = threading.Thread(target=sending_file, args=(connection,))
        thread.start()
