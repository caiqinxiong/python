# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/2 17:00
import re


def multiply_divide_compute(exp):
    '''乘除计算'''
    num_list = re.split("[*/]", exp)  # 根据*或/号切割式子，得到各个数字的list,如['7/3*99/4*2998']切割后为['7', '3', '99', '4', '2998']
    symbol = re.findall("[*/]", exp)  # 再获取一一对应的计算符号，['/', '*', '/', '*']
    ret = float(num_list[0])  # 从左到右依次计算，list第一个值赋给ret，然后去*或/下一个数，返回计算结果。
    for n in range(1, len(num_list)):
        if symbol[n - 1] == "*":
            ret *= float(num_list[n])
        elif symbol[n - 1] == "/":
            ret /= float(num_list[n])
    return ret


def add_subtract_compute(symbol, num_list):
    '''计算加减'''
    ret = float(num_list[0])  # 从左到右依次计算，list第一个值赋给ret，然后去+或-下一个数，返回计算结果。
    for n in range(1, len(num_list)):
        if symbol[n - 1] == "+":
            ret += float(num_list[n])
        elif symbol[n - 1] == "-":
            ret -= float(num_list[n])
    return ret


def change_symbol(exp):
    '''处理符号'''
    exp = exp.replace("++", "+")
    exp = exp.replace("+-", "-")
    exp = exp.replace("-+", "-")
    exp = exp.replace("--", "+")
    exp = exp.replace("- -", "+")
    exp = exp.replace("+ -", "-")
    return exp


def reduction_formula(symbol, multiply_divide):
    '''还原算式'''
    # 处理乘除算式中前面带负号的情况
    if len(multiply_divide[0].strip()) == 0:  # 切割后的list第一个值如果为空，则为负号，如-40/5切割后为['', '40/5']
        multiply_divide[1] = symbol[0] + multiply_divide[1]
        del multiply_divide[0]  # 把list的第一个空值删除掉
        del symbol[0]  # 负号已经拼接到上面的式子里了，所以要删除掉多余的负号。
    # 处理乘除算式中后面带负号的情况
    for index, f in enumerate(multiply_divide):
        # 9-2*5/3+7/3*99/4*-2998 +10 * 568/14 切割后为['9', '2*5/3 ', ' 7 /3*99/4*', '2998 ', '10 * 568/14 ']，循环list处理。
        f = f.strip()  # 去除算式中的左右空格
        if f.endswith("*") or f.endswith("/"):  # 如果以*或/结尾的式子，说明后面带-号被切割了，给还原一下。
            multiply_divide[index] = multiply_divide[index] + symbol[index] + multiply_divide[index + 1]  # 如：['', '40/', '5']还原为 ['-40/-5']
            del multiply_divide[index + 1]  # 将已拼接的值删除掉
            del symbol[index]  # 对应的负号也删除掉
    return symbol, multiply_divide


def compute(exp):
    '''计算'''
    # 先计算乘除，后算加减。
    multiply_divide = re.split("[+-]", exp)  # 按+或-切割，取出乘除算式，返回list。-40/5切割后为['', '40/5']，-40/-5切割后为['', '40/', '5']
    symbol = re.findall("[+-]", exp)  # 获取所有的+和—号，返回list，和上面的split的个数对应。-40/-5得到的值为['-', '-']
    symbol, multiply_divide = reduction_formula(symbol, multiply_divide)  # 调用符号处理函数，返回处理后的结果。
    # 开始计算乘除
    for index, f in enumerate(multiply_divide):  # 可能有多个，循环计算，如['9', '2*5/3 ', ' 7 /3*99/4*-2998 ', '10 * 568/14 ']
        if re.search("[*/]", f):  # 只计算乘除的式子，没有返回None。
            multiply_divide[index] = multiply_divide_compute(f)  # 调用乘除计算函数，每次传入的是只带*或/的式子，将计算结果返回对应的list中，如['-40/5']计算完返回['-8.0']

    # 开始计算加减
    # print(symbol,multiply_divide) #如['-', '+', '+'] ['9', 3.3333333333333335, -173134.50000000003, 405.7142857142857]
    ret = add_subtract_compute(symbol, multiply_divide)  # 将对应的+-符号和计算完乘除后的list再进行加减运算，返回最终的计算结果。
    return ret


def main(exp):
    '''主控制逻辑'''
    while True:
        parentheses = re.search("\([^()]*\)", exp)  # [^()]*表示不包含任意一个口号，既匹配最里层的括号，从右往左，匹配第一个。
        # print(parentheses) # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
        if parentheses != None:
            f = parentheses.group().strip("()")  # 去掉拓号，只保留算式。
            ret = compute(f)  # 计算括号里的式子并返回计算结果
            exp = exp.replace(parentheses.group(), str(ret))  # 计算完成后，把括号里的内容替换成计算结果
            exp = change_symbol(exp)  # 一个括号计算完成后可能产生负号，处理+-号，例如计算完第一个括号的结果为-8.0，1 - 2 * ( (60-30 +-8.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )，带了+-号。
        else:
            ret = compute(exp) # 没有括号了，直接计算剩下的数即可
            return ret


if __name__ == '__main__':
    # exp = '(-40/5)'
    # exp = '( 7 /3*99/4*2998 )'
    # exp = '(9-2*5/3 + 7 /3*99/4*-2998 +10 * 568/14 )'
    exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # 剔除空字符
    exp = re.sub(r'\s+', '', exp)
    ret = main(exp)
    print('算式%s的计算结果为：\n%s' % (exp, ret))
    print(eval(exp)) # 验证函数计算结果是否一致