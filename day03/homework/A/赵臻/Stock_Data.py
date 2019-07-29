#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time : 2019/7/22 0022 2:35
@Author : 赵臻
@File : Stock_Data.py
@Software: PyCharm
'''

# 定义data_Processing函数(读取数据并处理成字典的形式存入内存)
def data_processing():
    lst = []
    with open('stock_data.txt',mode='r',encoding='utf-8') as f:
        # for循环读取每一行
        for i in f:
            # 将每一行分别写入lst列表中
            lst.append(i.strip())
        # 取出字典的kay
        k = lst[0].split('|')
        dic_list = []
        for n in lst[1:]:
            v = n.split('|')
            # 使用zip函数将数据转为K,V的形式，然后用dict转为字典存入dic_list列表中
            dic_list.append(dict(zip(k,v)))
        # 将dic_list设置成返回值，以便后续调用
        return dic_list

# 定义输入查询的数据是大于的函数代码
def Data_Query_Gt(dic_list,inp):
    # 将输入的内容转换为列表赋值给inp_1
    inp_1 = inp.partition(">")
    row = 0
    # 循环dic_list字典
    for i in dic_list:
        # 取出类名相应的值
        value = i[inp_1[0]]
        # 判断取出大于对比值的数据
        if float(value) > float(inp_1[2]):
            print(i)
            row += 1
    if row == 0:
        print("sorry,你所查询的数据不存在,请重新查询")
    else:
        print("数据查找到：\033[031m%s\033[0m 条"%row)
# 定义输入查询的数据是小于的函数代码
def Data_Query_lt(dic_list,inp):
    # 将输入的内容转换为列表赋值给inp_1
    inp_1 = inp.partition("<")
    row = 0
    # 循环dic_list字典
    for i in dic_list:
        # 取出类名相应的值
        value = i[inp_1[0]]
        # 判断取出小于对比值的数据
        if float(value) < float(inp_1[2]):
            print(i)
            row += 1
    # 判断row是否为0，如为0则表示为查到数据
    if row == 0:
        print("sorry,你所查询的数据不存在,请重新查询")
    else:
        print("数据查找到：\033[031m%s\033[0m 条"%row)
# 定义用户输入股票查询接口
def data_query():
    # 调用dic_list字典
    dic_list = data_processing()
    print("\033[031m\t欢迎使用股票查询系统\033[0m")
    print("1、支持(\033[031m模糊查询\033[0m)\n2、支持(\033[031m项查询\033[0m)\n3、支持(\033[031mQ退出程序\033[0m)\
    \n4、查询项有：%s %s %s %s %s %s %s %s"\
          %("最新价","涨跌额","最高","最低","今开","昨收","市盈率","市净率"))
    # 判断输入的字符串中是否包含">"
    while True:
        # 用户输入要查询的判断字符串
        inp = input("股票查询接口>>> ")
        if ">" in inp:
            # 如果包含">",执行如下函数定义的代码
            Data_Query_Gt(dic_list,inp)
        # 判断输入的字符串中是否包含"<"
        elif "<" in inp:
            # 如果包含"<",执行如下函数定义的代码
            Data_Query_lt(dic_list,inp)
        # 赋值不用判断去模糊查找，如查到数据打印，没有则返回0条数据
        elif inp.upper() == "Q":
            print("查询结束,欢迎再次回来")
            break
            # 循环从dic_list取出key
        else:
            row = 0
            for key in dic_list:
                # 循环取出的key所对应的value
                for i in key:
                    # 判断value中是否包含用户输入的字符串
                    if inp in key[i]:
                        print(key)
                        row += 1
            if row == 0:
                print("sorry,你所查询的数据不存在,请重新查询")
            else:
                print("数据查找到：\033[031m%s\033[0m 条" % row)
data_query()



