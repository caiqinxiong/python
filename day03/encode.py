# -*- coding:utf-8 -*-
# Author:caiqinxiong
import sys
print(sys.getdefaultencoding())

name ="蔡亲雄"
print(name)
print(name.encode('utf-8'))
#print(name.decode('utf-8').encode('gbk'))#因为默认的文本字符串为unicode格式，因此文本字符串没有decode方法
#https://www.cnblogs.com/geekard/archive/2012/10/04/python-string-endec.html