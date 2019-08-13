import re
def mul_div(atom_exp):
    '''
    专门负责计算a*b或者a/b这样的表达式的函数
    :param atom_exp: a*b或者a/b的表达式
    :return:float数据类型的结果
    '''
    if '*' in atom_exp:
        a,b= atom_exp.split('*')
        return float(a) * float(b)
    elif '/' in atom_exp:
        a,b = atom_exp.split('/')
        return float(a) / float(b)

def add_sub(no_bracket_exp):
    '''
    接收一个只有加减法的表达式,计算加减法并返回最终结果
    :param no_bracket_exp: 只剩下加减法的表达式
    :return:float数据类型的返回值
    '''
    ret_lst = re.findall('[-+]?\d+(?:\.\d+)?', no_bracket_exp)   # [-8]
    sum_count = 0
    for num in ret_lst:
        sum_count += float(num)
    return sum_count

def exp_format(exp):
    '''
    负责表达式的整理
    :param exp:接收的表达式可能含有 ++ -- +- -+等操作
    :return:返回一个没有重叠+-符号的表达式
    '''
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('-+','-')
    exp = exp.replace('++','+')
    return exp

def cal(no_bracket_exp):
    '''
    负责计算加减乘除
    :param no_bracket_exp: 一个内部不再有括号的表达式
    :return:
    '''
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',no_bracket_exp)
        if ret:
            ret_exp = ret.group()   # ret_exp = '2*5'
            res = str(mul_div(ret_exp))
            no_bracket_exp = no_bracket_exp.replace(ret_exp,res)
        else: break
    no_bracket_exp = exp_format(no_bracket_exp)
    sum_count = add_sub(no_bracket_exp)
    return sum_count

def main(exp):
    exp = exp.replace(' ', '')
    while True:
        ret = re.search('\([^()]+\)', exp)
        if ret:
            no_bracket_exp = ret.group()
            ret = str(cal(no_bracket_exp))
            exp = exp.replace(no_bracket_exp, ret)
        else:break
    return cal(exp)

exp = '1 - 2 * ( (60-30 +  (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )* (-40/5)) - (-4*3)/ (16-3*2) )'
res = main(exp)
print(res)
# 一个事物不可再分了 原子
# 2*5



