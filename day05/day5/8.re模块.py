# 使用re模块 : 操作正则表达式
# 使用time模块 : 操作时间
# 使用random模块 : 操作随机数
# 正则指引 : python环境下使用的正则表达式规则

import re
# ret = re.findall('\d+','hello123,world456') # 匹配所有匹配项
# print(ret)

# ret = re.search('\d+','hello123,world456')   # 只匹配从左到右第一个匹配项
# print(ret)   # 变量
# print(ret.group())

# ret = re.findall('\d+(?:\.\d+)?','hello123.172,world456.234')
# print(ret)
# .172  .234