# -*- coding:utf-8 -*-
# Author:caiqinxiong
import sys
import os
import chardet


def parseArgs(sys_args=sys.argv):
    '''
    处理命令行参数传入
    :return:
    '''
    __diff_file = (lambda x: len(x) != 1 and x[1] or 'help')(sys_args)
    return __diff_file


def fun_controller(__diff_file):
    # 将所有的编码都转换成utf-8
    file_old = open(__diff_file, 'rb')
    file_new = open('tmp.diff', 'w')
    for buff in file_old.readlines():
        encode = chardet.detect(buff)
        str_encode = encode['encoding']
        buff = buff.decode(str_encode).encode("utf-8")
        file_new.write(buff)
    file_old.close()
    file_new.close()
    # 将转换后的文件再写回原文件
    cat_cmd = u'cat tmp.diff > %s ' % __diff_file
    os.system(cat_cmd)
    rm_cmd = u'rm -rf  tmp.diff'
    os.system(rm_cmd)


def main():
    # 1. 分析获取参数
    __diff_file = parseArgs()
    fun_controller(__diff_file)


if __name__ == '__main__':
    main()

