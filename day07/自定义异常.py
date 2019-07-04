# -*- coding:utf-8 -*-
# Author:caiqinxiong
class caiqinxiongException(Exception):#继承Exception基类
    pass
    # def __init__(self, msg):
    #     self.message = msg
    #
    # def __str__(self):
    #     return self.message

try:
    raise caiqinxiongException('我的异常')
except caiqinxiongException as e:
    print(e)