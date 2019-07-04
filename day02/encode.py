# -*- coding:utf-8 -*-
# Author:caiqinxiong

str = "人生苦短，我用python！"
print(str)
print(str.encode("utf-8"))
#转成二进制
str2 = str.encode("utf-8")
#从二进制转回utf-8
print(str2.decode('utf-8'))