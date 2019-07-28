s = 'alex今天去洗脚城遇到了wusir'
# 字符串 就是一堆字符组成一串
# 索引的
# s = 'alex今天去洗脚城遇到了wusir'
# print(s[0])
# print(s[-1])
# print(s[10])
# 切片
# print(s[0:4])
# print(s[:4])
# print(s[::-1])

# 字符串的循环
# for char in s:
#     print(char)

# 修改大小写
# s = 'q'
# print(s.upper())

# 让用户录入全班同学的名字
# l = []
# while True:
#     name = input('同学的名字 :')
#     if name.upper() == 'Q':
#         break
#     l.append(name)
#     print('已添加%s同学'%name)
# print(l)

# s2 = 'Q'
# print(s2.lower())


# 切割和合并
# s = 'alex|alex3714|83'
# l = s.split('|')
# print(l)

# s2 = '|'.join(['alex', 'alex3714', '83'])
# print(s2)

# 替换 replace
# s = 'wusir和wusir是一对儿好基友'
# s1 = s.replace('wusir','老王')
# print(s)
# print(s1)
# s2 = s.replace('wusir','老王',1)
# print(s)
# print(s2)

# 去掉边界上的内容 strip
# s1 = '   wa    haha   '
# print(s1.strip())

# usr = input('user :').strip()
# pwd = input('passwd :').strip()
# if usr == 'alex' and pwd == 'alex3714':
#     print('登陆成功')
# else:
#     print('登录失败')

# s2 = '<娃哈哈>'
# print(s2.strip('>'))
# print(s2.strip('<'))
# print(s2.strip('<>'))

# s3 = 'hello,apple'
# s4 = s3.strip('hello')
# print(s4)

# 判断字符串的开始和结尾
# s0 = '2019-9-10 17:02:22'
# s1 = '2019-9-10 17:02:23'
# s2 = '2019-9-10 18:02:22'
# print(s0.startswith('2019-9-10 17:02'))
# print(s1.startswith('2019-9-10 17:02'))
# print(s2.startswith('2019-9-10 17:02'))

# l = [s0,s1,s2]
# for s in l:
#     if s.startswith('2019-9-10 17'):
#         print(s)

# a = 'eating'
# b = 'sleeping'
# c = 'worked'
# l = [a,b,c]
# for word in l:
#     if word.endswith('ing'):
#         print(word)

#字符串的组成
# num = input('红球的号码 :')
# print(type(num))
# if num.isdigit():
#     num_int = int(num)
#     print(type(num_int))
# else:
#     print('请输入数字来确保程序正常运行')

# 判断这个字符串是不是完全由数字组成
# s1 = '12345'
# s2 = 'abc123'
# print(s1.isdigit())
# print(s2.isdigit())

# s1 = '12345'
# s2 = 'abc你好壹仟'
# print(s1.isalpha())
# print(s2.isalpha())


# s = '菠萝蜜苹果香蕉'
# print('香蕉' in s)
# print('菠萝蜜' in s)
# print('菠萝' in s)

# l = ['菠萝蜜','苹果','香蕉']
# print('香蕉' in l)
# print('菠萝蜜' in l)
# print('菠萝' in l)

# s = 'alex菠萝蜜苹果香蕉'
# print(len(s))


# 修改和赋值上的问题
# a = 'alex'
# b = a
# a = 'wusir'
# print(b)