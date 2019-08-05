# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/2 17:00
import re
import functools


def minus_operator_handler(num):
    '''处理一些特殊的减号运算'''
    minus_operators = re.split("-", num)
    calc_list = re.findall("[0-9]", num)
    if minus_operators[0] == '':  # 第一值肯定是负号
        calc_list[0] = '-%s' % calc_list[0]
    res = functools.reduce(lambda x, y: float(x) - float(y), calc_list)
    print("\033[33;1m减号[%s]处理结果:\033[0m" % num, res)
    return res


def change_symbol(num):
    num = num.replace("++", "+")
    num = num.replace("+-", "-")
    num = num.replace("-+", "-")
    num = num.replace("--", "+")
    num = num.replace("- -", "+")
    return num


def compute_mutiply_and_dividend(num):
    '''算乘除,传进来的是字符串噢'''
    operators = re.findall("[*/]", num)
    calc_list = re.split("[*/]", num)
    res = None
    for index, i in enumerate(calc_list):
        if res:
            if operators[index - 1] == "*":
                res *= float(i)
            elif operators[index - 1] == "/":
                res /= float(i)
        else:
            res = float(i)

    print("\033[31;1m[%s]运算结果=\033[0m" % num, res)
    return res


def handle_minus_in_list(operator_list, calc_list):
    '''有的时候把算术符和值分开后,会出现这种情况  ['-', '-', '-'] [' ', '14969037.996825399 ', ' ', '12.0/ 10.0 ']
       这需要把第2个列表中的空格都变成负号并与其后面的值拼起来,恶心死了
    '''
    for index, i in enumerate(calc_list):
        if i == '':  # 它其实是代表负号,改成负号
            calc_list[index + 1] = i + calc_list[index + 1].strip()


def reduction_formula(symbol, multiply_divide):
    '''还原算式'''
    # 处理乘除算式中前面带负号的情况
    if len(multiply_divide[0].strip()) == 0:  # 切割后的list第一个值如果为空，则为负号，如-40/5切割后为['', '40/5']
        multiply_divide[1] = symbol[0] + multiply_divide[1]
        del multiply_divide[0] # 把list的第一个空值删除掉
        del symbol[0] # 负号已经拼接到上面的式子里了，所以要删除掉多余的负号。
    # 处理乘除算式中后面带负号的情况
    for index, i in enumerate(multiply_divide): #9-2*5/3+7/3*99/4*-2998 +10 * 568/14 切割后为['9', '2*5/3 ', ' 7 /3*99/4*', '2998 ', '10 * 568/14 ']
        i = i.strip()
        if i.endswith("*") or i.endswith("/"):
            multiply_divide[index] = multiply_divide[index] + symbol[index] + multiply_divide[index + 1]
            del multiply_divide[index + 1]
            del symbol[index]
    return symbol, multiply_divide


def compute(num):
    '''计算'''
    # 先计算乘除，后算加减。
    multiply_divide = re.split("[+-]", num)  # 按+或-切割，取出乘除算式，返回list。-40/5切割后为['', '40/5']，-40/-5切割后为['', '40/', '5']
    symbol = re.findall("[+-]", num) # 获取所有的+和—号，返回list，和上面的split的个数对应。-40/-5得到的值为['-', '-']
    print("*"*200)
    print(multiply_divide)
    print(symbol)
    symbol, multiply_divide = reduction_formula(symbol,multiply_divide)
    print(symbol, multiply_divide)
    exit(-1)
    for index, i in enumerate(multiply_divide):
        if re.search("[*/]", i):
            sub_res = compute_mutiply_and_dividend(i)
            multiply_divide[index] = sub_res

    # 开始运算+,-
    print(multiply_divide, symbol)
    total_res = None
    for index, item in enumerate(multiply_divide):
        if total_res:  #代表不是第一次循环
            if symbol[index - 1] == '+':
                total_res += float(item)
            elif symbol[index - 1] == '-':
                total_res -= float(item)
        else:
            total_res = float(item)
    print("\033[32;1m[%s]运算结果:\033[0m" % num, total_res)
    return total_res


def main(num):
    '''主控制逻辑'''
    while True:
        parentheses = re.search("\([^()]*\)", num)  # [^()]*表示不包含任意一个口号，既匹配最里层的括号，从右往左，匹配第一个。
        # print(parentheses) # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
        if parentheses != None:
            num = parentheses.group().strip("()")  # 去掉拓号，只保留算式。
            print(num)
            ret = compute(num) # 计算括号里的式子并返回计算结果
            ret = change_symbol(ret)  # 计算完成后可能产生负号，去除外重复的+-号
            num = num.replace(num, str(ret)) # 计算完成后，把括号里的内容替换成计算结果
        else:
            # 没有括号了，直接计算剩下的数即可
            ret = compute(num)
            print('\n\n\033[42;1m最终结果:\033[0m', ret)
            break


if __name__ == '__main__':
    exp = '(9-2*5/3 + 7 /3*99/4*-2998 +10 * 568/14 )'
    #exp = '(-40/-5)'
    #exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    #exp ="1 - 2 * ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    res = main(exp)