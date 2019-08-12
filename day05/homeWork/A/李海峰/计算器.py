#李海峰
exp='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
exp=exp.replace(' ','')#除去空格
import re
#乘法除法计算
def mul_di(ex):
    if '/' in ex:
        a,b = ex.split('/')
        return str(float(a)/float(b))
    elif '*' in ex:
         a,b = ex.split('*')
         return str(float(a)*float(b))
#计算小括号里边的乘除法，获取结果替换原来的值
def mul_div(ex):
    while True:
        ret=re.search('\d+(?:\.\d+)?[/*]-?\d+(?:\.\d+)?',ex)
        if ret:
            value=ret.group()
            new_value=mul_di(value)
            ex=ex.replace(value,new_value)
        else:
            break
    return ex
#带有以下符号内容的进行替换
def mul_d(ex):
    ex=ex.replace('++','+')
    ex=ex.replace('+-','-')
    ex=ex.replace('-+','-')
    ex=ex.replace('--','+')
    return ex
#循环，计算括号内的值，并去除括号
def Ubk_cal(ex):
    ret=re.findall('[+-]?\d+(?:\.\d+)?',ex)
    count=0
    for i in ret:
        count+=float(i)
    return str(count)
#找到最里边的括号，进行计算，再执行最外侧括号
def all(ex):
    while True:
        nu = re.search('\([^()]+\)',ex)
        if nu:
            ret=nu.group()
            value=mul_div(ret)
            value=mul_d(value)
            new_val=Ubk_cal(value)
            ex=ex.replace(ret,new_val)
        else:
            break
    ret=mul_div(ex)
    value=mul_d(ret)
    return Ubk_cal(value)
print(all(exp))