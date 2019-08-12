'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-08 16:22:09
@LastEditTime: 2019-08-09 18:42:05
@LastEditors: Please set LastEditors
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time : 2019/8/8 0008 11:03
@Author : 赵臻
@File : sum_num.py
@Software: PyCharm
'''
import re


# 计算乘除的方法
def parse_exp(exp):
    if "*" in exp:
        a, b = exp.split("*")
        return str(float(a) * float(b))

    if "/" in exp:
        a, b = exp.split("/")
        return str(float(a) / float(b))


# 去除++ +- -- -+
def exp_format(exp):
    exp = exp.replace("+-", "-")
    exp = exp.replace("--", "+")
    exp = exp.replace("-+", "-")
    exp = exp.replace("++", "+")
    return exp


# 实际计算
def exp_calc(source):
    # 计算乘除
    while True:
        ret_obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?", source)
        if ret_obj:
            ret = ret_obj.group()
            ret2 = parse_exp(ret)
            source = source.replace(ret, ret2)
        else:
            break
    # 计算加减
    ret = exp_format(source)
    lst = re.findall(r"[+-]?\d+(?:\.\d+)?", ret)
    count = 0
    for i in lst:
        count += float(i)
    return count


# 去除括号
def remove_parentheses(source):
    while True:
        ret_obj = re.search(r"\([^()]+\)", source)
        if ret_obj:
            ret_exp = ret_obj.group()
            # 计算括号里面的值,exp_calc
            res = str(exp_calc(ret_exp))
            # 把算好的实际数值转换成字符串,替换以前的圆括号
            source = source.replace(ret_exp, res)
        else:
            # 直接返回替换好的字符串
            return source

# 主函数
def main(source):
    # 先把所有的空格去掉
    source = source.replace(" ", "")
    # 去除括号
    ret = remove_parentheses(source)
    # 计算结果
    return exp_calc(ret)


exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

ret1 = main(exp)
print("rec模块及正则计算结果：", ret1)
# 验证结果
print("eval计算结果：", eval(exp))