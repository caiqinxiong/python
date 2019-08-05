# -*- coding: utf-8 -*-
# 2019/8/5 13:56
# 参考女神博客链接：https://www.cnblogs.com/Eva-J/articles/11266790.html?tdsourcetag=s_pcqq_aiomsg#_label6
import random

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