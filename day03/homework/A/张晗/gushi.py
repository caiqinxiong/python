import prettytable as pt # 用来做展示的模块 需要安装(pip install prettytable)

# 定义一个函数fun，用来获取所有数据，以列表方式返回
def all_list(head='none'):
    with open('stock_data.txt',mode='r',encoding='utf-8') as f:
        if head == 'head':          # 获取第一行内容，去除多余的制表符及空格，增加至列表 ，作为表头
            ret = f.readline()
            f1 = ret.replace('\t', '|')
            f2 = f1.replace(' ', '').split('|')
            while '' in f2:
                f2.remove('')
            return f2
        else:
            f.readline()    # 先读取一行（表头），然后进行循环
            l1 = []
            for ret in f:
                # 去除空格及制表符，按老师要求用"|" 好像没用上
                f1=ret.replace('\t','|')
                f2=f1.replace(' ','').split('|')
                while '' in f2 :
                    f2.remove('')
                l1.append(f2)         #将每行内容追加进列表，不然无法正常返回
            return l1


# 定义一个根据模糊名称返回内容的函数
def named(chooise):
    ret = all_list()
    l =[]
    for i in ret:
        if chooise in i[2]:
            l.append(i)
    return l

'''
定义一个比较函数
'''
def contrast(chooise,sign,num):
    ret = all_list('head')
    l = []
    if sign == '<':
        for i in all_list():
            ret1 = i[ret.index(chooise)]
            if  float(ret1.strip('%')) < float(num.strip('%')):
                l.append(i)
        return l

    if sign == '>':
        for i in all_list():
            ret2 = i[ret.index(chooise)]
            if  float(ret2.strip('%'))> float(num.strip('%')):
                l.append(i)
        return l


def write(lst):
    tb = pt.PrettyTable()
    tb.field_names = all_list('head')
    for i in lst:
        tb.add_row(i)
    print(tb)


while True:
    chooise = input('分析接口>>>')
    for a in ['<','>']:
        if  a in chooise:
            lst = chooise.split(a)
            f=contrast(lst[0],a,lst[1])
            write(f)

    if chooise.upper() == 'Q':
        break
    if  '<'  not in chooise and '>' not in chooise:
        lst = named(chooise)
        write(lst)




