# -*- coding:utf-8 -*-
# Author:caiqinxiong
import shelve
import datetime
# 与 json 和 pickle类似
d = shelve.open('shelve_test') # 打开一个文件
# 将数据持久化序列
info = {'age': 28, 'job':'IT'} # 字典
name = ['cai','lixiaoxin','who'] # list
d['name'] = name # 持久化列表
d['info'] = info # 持久化字典
d['time'] = datetime.datetime.now()

# 将序列化的数据读取出来
# print(d.get('name'))
# print(d.get('info'))
# print(d.get('time'))
print(d.items())
for item in d.items():
    print(item)
    print(item[0])
    print(d[item[0]])
    print(''.center(50,'~'))

d.close()