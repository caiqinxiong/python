# -*- coding:utf-8 -*-
# Author:caiqinxiong
import re

res = re.match('^.+','Caiqinxiong123')# .代表一个字符，.+代表匹配多个字符,match从第一个开始匹配
res2 = re.match('..','Caiqinxiong123')# .代表一个字符，.+代表匹配多个字符
res3 = re.search('qin','Caiqinxiong123')# 从整个文本中搜索
res4 = re.search('q.+g','Caiqinxiong123')# 从整个文本中搜索
res4_1 = re.search('n.+x','Caiqinxiong123')# +匹配多次，中间没有找不到，不匹配
res4_2 = re.search('n.*x','Caiqinxiong123')# *匹配0到多次，匹配
res5 = re.search('[0-9]{3}','Cai1qin22xiong123')# {m}匹配几次
res6 = re.search('[0-9]{1,3}','Cai1qin22xiong123')# {n,m}匹配n到m次
res7 = re.findall('[0-9]{1,3}','Cai1qin22xiong123')# {n,m}匹配n到m次
print(res.group())
print(res2.group())
print(res3.group())
print(res4.group())
#print(res4_1.group())
print(res4_2.group())
print(res5.group())
print(res6.group())
print(res7)