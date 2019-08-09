# 常用模块

#1.验证码
import random
# 4位数字验证码  6位数字验证码
# 一位一位的生成，每一位都是0-9之间的随机数字，然后再把这些数字拼接在一起
# 纯数字的验证码
# def code(n=6):
#     s = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         s += str(num)
#     return s
#
# ret = code()
# print(ret)
# ret = code(4)
# print(ret)

# 4位数字+字母验证码  6位数字+字母验证码
# 123GH6
# a25b98
# 每一位都会随机生成一个数字和小写字母和大写字母，然后再从这三个随机生成的内容中抽取一个，拼起来
# chr(num)把一个num转换成一个对应的ascii码的字母 97+25=122 65+25 = 90
# def code(n):
#     s = ''
#     for i in range(n):
#         num = random.randint(0, 9)
#         alpha_lower = chr(random.randint(97,122))
#         alpha_upper = chr(random.randint(65,90))
#         res = random.choice([num,alpha_upper,alpha_lower])
#         s += str(res)
#     return s
# ret = code(6)
# print(ret)
# ret = code(4)
# print(ret)
#
# def code(n=4,alpha=True):
#     s = ''
#     for i in range(n):
#         num = random.randint(0, 9)
#         if alpha:
#             alpha_lower = chr(random.randint(97,122))
#             alpha_upper = chr(random.randint(65,90))
#             num = random.choice([num,alpha_upper,alpha_lower])
#         s += str(num)
#     return s
#
# ret = code()
# print(ret)
# ret = code(6)
# print(ret)
# ret = code(alpha=False)
# print(ret)
# ret = code(6,False)
# print(ret)


# 每一位上都有可能出现a-z/A-Z/1-9数字和字母


# 2.发红包 拼手气红包
# 200元 10个 每个人抢到的钱都是随机的
# 每一个人抢到多少钱的概率都平均
import random

# 0-20000之间随机取n个不重复的整数
# def send_money(money,n):
#     lst = []
#     money = money*100
#     ret = random.sample(range(1,money),n-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(money)
#     for i in range(len(ret)-1):
#         val = ret[i+1] - ret[i]
#         val = val/100
#         lst.append(val)
#     return lst
#
# print(send_money(100,5))

def send_money(money,n):  # money表示要发多少钱 ，n表示要发几个红包
    money = money*100
    ret = random.sample(range(1,money),n-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    for i in range(len(ret)-1):
        val = ret[i+1] - ret[i]
        val = val/100    # 分 转 元
        yield val
        money -= val*100
        print('红包余额:',money)
g = send_money(100,20)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())

# float之间的计算不准确

# 提供一个正则表达式
# 求一个表达式中不带其他括号的正则？？？
# 7-(1+2*(3+4-6))
# \([^()]+\)