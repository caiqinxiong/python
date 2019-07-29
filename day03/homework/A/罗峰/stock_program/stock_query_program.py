#python27期 罗锋
#调整格式，并把内容输入到文件
def adjustment_format():
    with open(r'stock_data.txt',mode='r',encoding='utf-8') as f1,\
        open(r'stock_data.txt.bak',mode='w',encoding='utf-8') as f2:
        # first_line=f1.readline()
        for line in f1:
            line=line.strip()
            lst=line.split('\t')
            lst.pop(3)
            lst1='|'.join(lst)+'\n'
            print(lst1)
            f2.write(lst1)
#查询股票数据，并把文件内容转化为列表
def query_stock():
    ls = []
    with open(r'stock_data.txt.bak', mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            lst = line.split('|')
            # print(lst)
            # print(lst)
            ls.append(lst)
        return ls
#模糊匹配输出要查询的股票
def select(choose_stock):
    stock=query_stock()
    for l1 in stock:
        if choose_stock in l1[2]:
            print(l1)
#通过股票价格、涨跌幅、换手率、市盈率这几列来筛选信息
def compare(str,symbol,num):
    stock=query_stock()
    if symbol == '>':
        if str == "最新价":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[3].strip('%')) > float(num):
                    print(l1)
        elif str == "涨跌幅":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[4].strip('%')) > float(num):
                    print(l1)
        elif str == "换手率":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[-3].strip('%')) > float(num):
                    print(l1)
        elif str == "市盈率":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[-2].strip('%')) > float(num):
                    print(l1)
    elif symbol == '<':
        if str == "最新价":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[3].strip('%')) < float(num):
                    print(l1)
        elif str == "涨跌幅":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[4].strip('%')) < float(num):
                    print(l1)
        elif str == "换手率":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[-3].strip('%')) < float(num):
                    print(l1)
        elif str == "市盈率":
            print(stock[0])
            for l1 in stock[1:]:
                if float(l1[-2].strip('%')) < float(num):
                    print(l1)
#主程序
def format_lst():
    while True:
        choose_stock=input('股票查询接口>>:')
        for symbo in ['>','<']:
            if symbo in choose_stock:
                str,num=choose_stock.split(symbo)
                compare(str,symbo,num)
        if choose_stock.find('股票') != -1:
            adjustment_format()
        elif choose_stock.upper() == 'Q':
            break
        else:
            lst=select(choose_stock)
format_lst()






