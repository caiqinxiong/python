# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/9 10:22
'''
# 2.发红包 拼手气红包
# 200元 10个 每个人抢到的钱都是随机的
# 每一个人抢到多少钱的概率都平均
'''
import random

# 0-20000之间随机取n个不重复的整数
def send_money(money,n):
    lst = []
    money = money*100
    ret = random.sample(range(1,money),n-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    for i in range(len(ret)-1):
        val = ret[i+1] - ret[i]
        val = val/100
        lst.append(val)
    return lst

print(send_money(100,5))

def red_envelope(money=200,n=10): # money表示要发多少钱 ，n表示要发几个红包
    '''抢红包'''
    money = money * 100 # 可以抢到分，将钱数乘以100，返回值时再除以100就能取到分了。
    line_list = random.sample(range(1,money),n-1) # sample不重复 的从1-199中随机取9个数，返回list。
    line_list.sort() # 将list从小到大排序
    line_list.insert(0,0) # 在list最前面插入0
    line_list.append(money) # 在list最后面加入200，list的长度为11，这样就能完整的在0-200区间获取10个红包了，list之间的值加起来刚好为200。
    for i in range(len(line_list)-1):
        red = line_list[i+1] - line_list[i] # 第二个点减去第一个点的值作为第一个红包，以此类推。
        red = red/100 # 再把分转换成元
        yield red # 利用生成器来节省内存使用
        # money = money - red*100
        # print('红包余额:',money/100)


if __name__ == '__main__':
    money=50
    n=10
    red = red_envelope(money,n)
    for i in range(n):
        print('第%s个红包%s元！'% (i+1,red.__next__()))

    # res=list(red)
    # print(res)
    # print(sum(res))