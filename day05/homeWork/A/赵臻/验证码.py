'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-05 16:06:36
@LastEditTime: 2019-08-09 18:35:59
@LastEditors: Please set LastEditors
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File  :  验证码.py
@Time  :  2019/08/05 16:06:38
@Author:  赵臻 
'''
import random

def Verification_code(val):
    row = 0
    # 循环6次,验证码位数
    while row < val:
        row += 1
        # 获取随机数字并且将数字转为字符串类型
        num = str(random.randint(0,9))
        # 获取随机小写字母,ASC中,a:91~z:122
        zimu_lower = chr(random.randint(97,122))
        # 获取随机大写字母,ASC码中:A:65~Z:90
        zimu_upper = chr(random.randint(65,90))
        # 随机产生一个内容
        num_zimu = [num,zimu_lower,zimu_upper]
        # 生成(数字+字母)共6位的
        ret = random.choice(num_zimu)
        print(ret,end='')
# Verification_code()
num_input = int(input("请输入你需要的验证码位数： "))
Verification_code(num_input)