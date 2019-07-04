# -*- coding:utf-8 -*-
# Author:caiqinxiong
import random
# 生成一个4位随机验证码
yan=''
for i in range(4):
    #current=random.randint(0,9) #生成0-9的随机数
    current=random.randrange(0,4) # 生成0-4的随机数，如果和i相等，随机添加字母或数字
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    yan+=str(tmp)
print("\n生成的4位随机验证码为：", yan)