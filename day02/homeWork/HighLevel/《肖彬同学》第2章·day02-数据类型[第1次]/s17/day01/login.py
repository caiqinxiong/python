#!/usr/bin/python
# -*- coding:utf-8 -*-
# 1. 打开并读取文件内容
f1 = open('db','r')
data = f1.read()
f1.close()

# 2. 格式化，列表中嵌套字典
print(data)
user_info_list = []
user_str_list = data.split('\n')
for item in user_str_list:
    temp = item.split('|')
    v = {
        'name': temp[0],
        'pwd': temp[1],
        'times': temp[2]
    }
    user_info_list.append(v)
user_info_list[1]['times'] = 3
print(user_info_list)

# 3. 列表中嵌套的字典


#
# 4. 重新写入文件
target = """alex|123123|3\neric|123123|3"""

f2 = open('db','w')
f2.write(target)
f2.close()