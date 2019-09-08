#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/4'

import json

class FileReadWrite():
    @staticmethod
    def file_read(filename):
        '''读取文件'''
        with open(filename,mode='r') as fp:
            for i in fp:
                u_info = json.loads(i)
                yield u_info

    @staticmethod
    def file_write(filename, content):
        '''写入文件'''
        with open(filename, 'a') as fw:
            ret = json.dumps(content)
            fw.write('%s\n'%ret)
