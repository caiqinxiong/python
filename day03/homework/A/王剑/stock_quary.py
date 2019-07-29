#!/usr/bin/env python
#Author:Mike.Laowang

from prettytable import PrettyTable as pt

#导入文件并处理数据结构
lst_stock = []
with open('stock_info.txt','r',encoding="utf-8") as f:
    l_title=f.readline().strip().split('\t')
    for line in f:
        lst = line.strip().split('\t')
        stock_info = {}
        for i in range(0,len(l_title)):
            stock_info[l_title[i]]=lst[i]
        lst_stock.append(stock_info)


##根据名称搜索，判断字符合法性暂时省略，输入数字会报错
def select(name):
    ptable = pt(l_title)
    print("select:", name)
    count = 0
    for item in lst_stock:

        if name in item['名称']:
            items = []
            for i in item:
                items.append(item[i])
            ptable.add_row(items)
            count += 1
    print(ptable)
    print('共找到%s条'%count)


def compare(name,mark,num):
    ptable = pt(l_title)

    print("select:",name,mark,num)
    count = 0
    if name in l_title:
        for item in lst_stock:
            if mark == ">":
                if float(item[name]) > float(num):
                    items = []
                    for i in item:
                        items.append(item[i])
                    ptable.add_row(items)
                    count += 1
            else:
                if float(item[name]) < float(num):
                    items = []
                    for i in item:
                        items.append(item[i])
                    ptable.add_row(items)
                    count += 1
    print(ptable)
    print('共找到%s条' % count)



#

if __name__ == "__main__":
    sql = ""
    while sql.upper() != 'Q':
        sql = input('股票查询接口(退出请按q)>>:')
        if sql.upper() == 'Q':
            print("谢谢使用,再见")
        elif sql.isalpha():
            a=select(sql)
        else:
            if '<' in sql:
                l = sql.strip().split('<')
                a = compare(l[0], '<', l[1])

            else:
                l = sql.strip().split('>')
                a = compare(l[0], '>', l[1])