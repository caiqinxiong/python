# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:42
import shelve
import hashlib

class Common:
    '''公共类'''
    def __init__(self):
        pass

    @staticmethod
    def writeInfo(file,name,content):
        '''写入信息'''
        with shelve.open(file,writeback=True) as s:
           s[name] = content

    @staticmethod
    def readInfo(file):
        '''读取信息'''
        with shelve.open(file,writeback=True) as s:
            for key, value in s.items():
                yield key, value # 返回生成器，节省内存

    @staticmethod
    def changeHashlib(password):
        '''将明文转换成密文'''
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        ret = md5.hexdigest()
        return ret
