# -*- coding:utf-8 -*-
# Author:caiqinxiong
import random
print(random.random())# 生成一个0到1之间到一个随机数[0,1)
print(random.randint(1,5)) #生成1到5到一个随机整数
print(random.randrange(1,5)) #生成1到4到一个随机整数
print(random.randrange(3)) #生成0,1,2随机整数
print(random.choice('caiqinxiong')) # 从字符串中随机找一个
print(random.choice([1,3,6])) # 从列表中随机找一个
print(random.sample('caiqinxiong',2))# 随机取两位，返回列表
print(random.uniform(1,3))# （1，3）之间到浮点数
LIST=[1,2,3,4,5,6]
print(LIST)
random.shuffle(LIST) # 洗牌，把列表打乱,不能赋值给变量，返回none
print(LIST)
