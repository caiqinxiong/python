# -*- coding: utf-8 -*-
# 2019/8/5 13:56
# 参考女神博客链接：https://www.cnblogs.com/Eva-J/articles/11266790.html?tdsourcetag=s_pcqq_aiomsg#_label6
import random
import string
from random import choice
# 小白版
yan=''
for i in range(4):
    #current=random.randint(0,9) #生成0-9的随机数
    current=random.randrange(0,4) # 生成0-4的随机数，如果和i相等，随机添加字母或数字
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    yan+=str(tmp)
print("生成的4位随机验证码为：", yan)

# 女神版
def verification_code():
    '''生成随机验证码'''
    code = ''  # 初始化验证码的值为空
    for i in range(4):  # 循环获取4个随机数，生成4位随机验证码
        num = random.randint(0, 9)  # 生成0-9的随机数
        alf = chr(random.randint(65, 90))  # 随机生成大小写字母，通过字母的ascii值获取
        tmp = random.choice([num, alf])  # 随机在数字和字母中获取一位字符
        # code = "".join([code, str(tmp)])  # 将随机获取的字符拼接
        code +=str(tmp)

    return code

yan = verification_code()
print("生成的4位随机验证码为：", yan)

# 升级版
def code(n=4,alpha=True):
    '''自定义版'''
    s = ''
    for i in range(n):
        num = random.randint(0,9)
        if alpha:
            alpha_lower = chr(random.randint(97,122))
            alpha_upper = chr(random.randint(65,90))
            num = random.choice([num,alpha_lower,alpha_upper])
        s += str(num)
    return s
# 默认生成4位，带大小写的随机验证码
ret = code()
print(ret)
# 生成8位带数字大小写字母的随机验证码
ret = code(8)
print(ret)
# 生成4位随机数字验证码
ret = code(alpha=False)
print(ret)
# 生成8位随机数字验证码
ret = code(8,False)
print(ret)

# 终极版
def Makepass(length=8, chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

ret = Makepass()
print(ret)
ret = Makepass(4)
print(ret)
ret = Makepass(4,chars=string.digits)
print(ret)

