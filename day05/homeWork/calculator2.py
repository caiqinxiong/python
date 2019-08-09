#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def deal_mul_divi(string):
    """
    处理乘除法
    只处理传过来的字符串，每次处理一个，返回字符串
    :param string: 字符串格式严格要求为 25/-5 或 34*3 这样，否则返回None
    :return: 返回处理后的结果字符串
    """
    res1 = re.search('\d+\.?\d*\/(\-|\d+\.?\d*)+', string)
    res2 = re.search('\d+\.?\d*\*(\-|\d+\.?\d*)+', string)
    if not res1 and not res2:
        print('格式有误：{}'.format(string))
        return None
    else:
        items = re.findall('\d+\.?\d*', string)
        result = str(float(items[0]) / float(items[1])) \
        if res1 else str(float(items[0]) * float(items[1]))
        #如果字符串中有- 负号，那就增加标记值，让返回值为负 re.search('-', string)同下 '-' in
        result = '-{}'.format(result) if '-' in string else result
        return result

def deal_plus_minus(string):
    """
    将没有乘除号的带（不带）括号都行的字符串传入。该函数先处理字符串中所有负数：(40-4+34)
    再处理所有正数，再用正数减负数值作为结果返回，操作皆为浮点数。
    :param string: 参数为只有 + - 号的算式
    :return:
    """
    if re.search('\*|\/', string):  #如果有乘除号视为错误
        return None
    num_minus = 0
    for minus in re.findall('\-(\d+\.?\d*)', string):  #将所有负数找出来并加起来
        string = string.replace(minus, 'sep')  #所有前面带减号的数，都将被sep 符替换
        num_minus += float(minus)
    num_plus = 0
    for plus in re.findall('(\d+\.?\d*)', string):  #匹配正数相加 #|\+(\d+\.?\d*)
        num_plus += float(plus)
    return str(num_plus - num_minus)

def match_brackets(string):
    """
    匹配算式中的括号，并调用函数处理
    :param string: 算式字符串
    :return:
    """
    flag = True
    while flag:
        brackets_str = re.search('\((\+|\-|\.|\/|\*|\d)+\)', string)  #拿到括号字符串
        if not brackets_str:
            flag = False
            continue
        else:
            result = deal_brackets(brackets_str.group())  #调用处理括号函数，处理返回
            # print('\033[33;1m{}\033[0m'.format(string))
            string = string.replace(brackets_str.group(), result, 1)  #将计算原括号得到的结果替换原括号
            # print('\033[34;1m{}\033[0m'.format(string))
            string = re.sub('(\+\-)|(\-\+)', '-', string)  #处理 +- 号和 -+ 并排一起
            string = re.sub('--', '+', string)  #处理 -- 两减号并排
            return string


def deal_brackets(string):
    """
    处理传过来的括号
    :param string:
    :return:
    """
    flag = True

    while flag:
        # ( -3.2/-1.6-2-3*-2)这样的也要能匹配得 3.2/-1.6
        mul_divi_str = re.search('(\d+\.?\d*)(\*|\/)(\-|\d+\.?\d*){1,2}', string)  #只能匹配一到两位如 - 1.6
        if not mul_divi_str:
            flag = False
            break
        else:
            # print('\033[31;4m处理传来的乘除:{}\033[0m'.format(mul_divi_str.group()))
            mul_divi_res = deal_mul_divi(mul_divi_str.group())
            string = string.replace(mul_divi_str.group(), mul_divi_res, 1)
            string = re.sub('(\+\-)|(\-\+)', '-', string)  # 处理 +- 号和 -+ 并排一起
            string = re.sub('--', '+', string)  # 处理 -- 两减号并排
            return deal_plus_minus(string)


def calculate(string):
    strip_space = lambda x: re.sub(' ', '', x, count=x.count(' '))  #将算式中的所有空格剔除
    string = strip_space(string)
    string = match_brackets(string)  #处理完表达式所有的的括号
    result = deal_brackets(string)  #在把没有括号的表达式交给它处理一次
    return result

parser_str = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print('\033[31;1meval:\033[0m{: >22}'.format(eval(parser_str)))  #eval 验证结果
print('\033[32;2mcalculate:\033[0m{}'.format(calculate(parser_str)))  #正则计算

