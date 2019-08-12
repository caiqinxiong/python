'''作业：计算器
完成人：Python27期刘晓松
使用方法：正则、递归
大致思路： 函数1：计算+-*/，后续所有计算最终都要使用此函数，
          函数2：计算类似1-2+3*4/5，正则先匹配*/，在匹配+-，然后调用函数1算，得出来结果replace掉正则匹配，然后掉函数2递归，
          函数3：搞最后的大的exp，先正则匹配出括号内的，去调函数2计算，计算的结果在replace，然后调用函数3递归。
实现功能：100%
完成时间：2019年8月9日'''

import re
def jianfa(exp):
    '''此函数：用于减法计算'''
    if exp.count("-")>2:
            exp=exp.replace("--","+")
            a,b=exp.split("+")
            a,b=float(a),float(b)
            return a+b
    elif exp.count("-")>1:
        if "--" in exp:
            exp=exp.replace("--","+")
            a,b=exp.split("+")
            a,b=float(a),float(b)
            return a+b
        else:
            exp=exp.strip("-")
            a,b=exp.split("-")
            a,b=float(a),float(b)
            return 0-(a+b)
    else:
        exp=exp.strip("-")
        a,b=exp.split("-")
        a,b=float(a),float(b)
        return a-b

def jisuanqi(exp):
    '''此函数：用于加减乘除计算'''
    if "*" in exp:
        a,b=exp.split("*")
        a,b=float(a),float(b)
        return a*b
    elif "/" in exp:
        a,b=exp.split("/")
        a,b=float(a),float(b)
        return a/b
    elif "+" in exp:
        a,b=exp.split("+")
        a,b=float(a),float(b)
        return a+b
    elif "-" in exp:
        return jianfa(exp)
def compute_replace(exp,ret):
    '''此函数：用于调用jisuanqi，然后得出的记过然后替换正则匹配的结果'''
    new_ret = jisuanqi(ret)
    new_ret = str(new_ret)
    new_exp = exp.replace(ret, new_ret)
    return new_exp
def fmt(exp):
    '''此函数：用于去除以下特殊的符号，避免正则匹配出错'''
    while "++" in exp or "--" in exp or "+-" in exp or "-+" in exp:
        exp= exp.replace("++","+")
        exp= exp.replace("--","+")
        exp= exp.replace("+-","-")
        exp= exp.replace("-+","-")
    return exp
def func_compute(exp):
    '''此函数：用于计算如1+2*/5这样的连续算法，先匹配*/在匹配+-,然后调用jisuanqi计算，并递归'''
    exp=fmt(exp)
    if "*" in exp or "/"  in exp:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp).group()
        new_exp=compute_replace(exp,ret)
        t_n_exp = func_compute(new_exp)    #计算出的结果，再去递归调用本函数
        return t_n_exp
    elif  "+" in exp or "-" in exp:
        if exp.startswith("-") and exp.count("-") ==1 and exp.count("+")==0:    #考虑如果最后结果为负数，走这个判断
            return exp
        ret = re.search('-?\d+(\.\d+)?[+-]\d+(\.\d+)?',exp).group()
        new_exp = compute_replace(exp, ret)
        t_n_exp = func_compute(new_exp)     #计算出的结果，再去递归调用本函数
        return t_n_exp
    else:
        return exp
def match(exp):
    '''此函数：正则匹先配出括号内的公式，然后去调用上面函数计算，并递归'''
    exp=exp.replace(" ","")
    if "(" in exp:
        match_exp=re.search("\([^()]+\)",exp).group()
        n_match_exp=match_exp.strip("(")
        n_match_exp = n_match_exp.strip(")")
        ret=func_compute(n_match_exp)
        new_exp=exp.replace(match_exp,ret)
        c_new_exp=match(new_exp)
        return c_new_exp
    else:
        return func_compute(exp)
exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
b=match(exp)
print(b)
print(eval(exp))

