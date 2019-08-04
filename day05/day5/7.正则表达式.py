# 正则表达式 是什么?
#     # 前端
#     # python
#     # java

# 正则表达式 : 只和字符串打交道
    # 第一: 从一大段文字中,获取符合条件的内容
        # 爬虫
    # 第二: 检测某一个字符串,是否完全符合规则
        # 表单的验证
            # 并不会真的请求银行,具体手机,具体的邮件
            # 总是根据一些规则来先判断是否合法

# while True:
#     phone_number = input('please input your phone number ： ')
#     if len(phone_number) == 11 \
#             and phone_number.isdigit()\
#             and (phone_number.startswith('13') \
#             or phone_number.startswith('14') \
#             or phone_number.startswith('15') \
#             or phone_number.startswith('16') \
#             or phone_number.startswith('17') \
#             or phone_number.startswith('18')\
#             or phone_number.startswith('19')):
#         print('是合法的手机号码')
#     else:
#         print('不是合法的手机号码')

# import re
# phone_number = input('please input your phone number ： ')
# if re.match('^(13|14|15|16|17|18|19)[0-9]{9}$',phone_number):
#         print('是合法的手机号码')
# else:
#         print('不是合法的手机号码')

# 字符组
# 匹配所有数字:[1-9]
# 匹配所有小写字母:[a-z]
# 匹配所有大写字母:[A-Z]
# 匹配所有字母数字:[0-9a-zA-Z]
# 只能从ascii码小的值到大的值,可以一次取多个区间:[0-9a-f]

# 元字符
# \d   [0-9]
# \w   [0-9a-zA-Z_] 中文?
# \s \t \n  匹配所有的空白符\制表符\换行符
# \D \W \S 匹配所有非数字\匹配所有非数字字母下划线\匹配所有非空白
# .    匹配除了换行符之外的任意一个字符
# ^ $  匹配一个字符串的开始,$匹配一个字符串的结束
# [] [^] 字符组 非字符组
# | () 或  用来规范符号的作用域

# 量词
# {n}  表示匹配n次
# {n,} 表示匹配至少n次
# {n,m} 表示匹配n-m次
# ?    0或1次
# +    1-无穷大
# *    0-无穷大

# 贪婪和惰性
# 尽量多的匹配
# 量词后面的?表示惰性匹配,会在符合条件的基础上尽量少的匹配内容

# 转义符
# 所有的特殊字符都需要转义才能恢复本来的意思

# 匹配手机号 :1[3-9]\d{9}
# 匹配任意的正整数 : [1-9]\d*
# 匹配任意的小数 : \d+\.\d+
# 匹配整数或小数 : \d+(\.\d+)?

# 只写元字符  一个元字符表示一位字符上的内容
# 元字符量词 量词只约束前面的一个元字符\
# (元字符元字符)量词








