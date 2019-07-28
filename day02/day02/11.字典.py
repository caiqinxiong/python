# d = {
#  'alex':'alex3714',
#  'wusir':'666',
#   'alex10000':'222222'
#  }
# print(d['alex'])
# print(d['alex10000'])
# 登录

# username = input('username :')
# password = input('password :')
# if username in d and d[username] == password:
#     print('登录成功')
# else:
#     print('登录失败')

d = {
 'alex':'alex3714',
 'wusir':'666',
  'alex10000':'222222'
 }
# username = 'alex'
# d[username]  # d['alex']
# 'alex':'alex3714'  k-v
# k-v
  # 永远是通过key找value

# 增
# d['老王'] = '999'
# print(d)
# d['老王'] = '感冒灵'
# print(d)
# # 删
# d.pop('alex')
# print(d)

# del d['alex']
# print(d)
# # 改
# d['wusir'] = '777'
# # 查
# print(d['wusir'])
# print(d)

# 字典的key是有要求的
 # 不能重复写两个key
 # key必须是可hash的：
    # 可以通过一个哈希算法计算出一个变量的哈希值
    # 不能做字典的key ：list dict set
# d = {'alex':84,'alex':73,123:['a','b'],(1,2,3):{'k':'v'}}
# d['alex'] = 125
# print(d)

# 字典的循环
# for i in d:
#   print(i,d[i])


d = {'k1':'v1'}
print('k1' in d)
print('v1' in d)
# d['k2']  # KeyError: 'k2'
print(d.get('k1'))
print(d.get('k2'))