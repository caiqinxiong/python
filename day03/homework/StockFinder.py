# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/21 下午10:30
def getData():
    '''获取源数据'''
    stock_data_list = []
    with open(r'stock_data.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                #print(line.split())
                # for j in line.split():
                #     print(j.center(7),end='')
                # print()
                print('|'.join(line.split()))
                stock_data_list.append(line.split())
        print('~' * 100)
    return stock_data_list


def changeData(data):
    '''数据转换'''
    if not data.find('万') < 0:
        data = float(data.split('万')[0]) * 10000
    elif not data.find('亿') < 0:
        data = float(data.split('亿')[0]) * 100000000
    elif not data.find('%') < 0:
        data = float(data.split('%')[0]) * 0.01
    else:
        if data.isdigit() or data.split(".")[1].isdigit():
            return float(data)
        else:
            print('输入有误啊！')
            return data
    return data


def printList(listData):
    '''打印列表'''
    if len(listData) == 0:
        print('\033[31;1m无查询结果！\033[0m')
    else:
        print('一共搜索到\033[31;1m%s\033[0m条结果，详情如下：' % len(listData))
        print('~' * 100)
        print('|'.join(data_list[0]))
        for i in listData:
            print('|'.join(i))
        print('~' * 100)


def compareData(compare, num, index, data_list):
    '''比较查询'''
    num_list = []
    # 获取比较完成数据，添加到列表里
    for i in range(1, len(data_list)):
        if compare == '<':
            if changeData(data_list[i][int(index)]) < float(num):
                num_list.append(data_list[i])
        else:
            if changeData(data_list[i][int(index)]) > float(num):
                num_list.append(data_list[i])

    # 打印比较结果
    printList(num_list)


def stockFinder(*args):
    '''比较查找数据'''
    # print(args)
    name = args[0][0]
    data_list = args[-1][-1]
    try:
        compare = args[0][1]  # 比较符号
        num = args[0][2]  # 比较数据
        # 获取输入项名称，支持模糊查找
        for i in data_list[0]:
            if not i.find(name) < 0:
                index = data_list[0].index(i)  # 获取该名称对应的index值
                compareData(compare, num, index, data_list)
    except:
        find_data = []
        # 模糊查找
        for i in range(1, len(data_list)):
            if not data_list[i][2].find(name) < 0:
                find_data.append(data_list[i])
        # 打印查找结果
        printList(find_data)


def checkArgs(data_list):
    '''校验传入参数'''
    choise = input('股票查询接口(按q退出)>>:').strip()
    if not choise.find('>') < 0:
        name = choise.split('>')[0].strip()
        num = choise.split('>')[-1].strip()
        num = changeData(num)
        return name, '>', num, data_list
    elif not choise.find('》') < 0:
        name = choise.split('》')[0].strip()
        num = choise.split('》')[-1].strip()
        num = changeData(num)
        return name, '>', num, data_list
    elif not choise.find('<') < 0:
        name = choise.split('<')[0].strip()
        num = choise.split('<')[-1].strip()
        num = changeData(num)
        return name, '<', num, data_list
    elif not choise.find('《') < 0:
        name = choise.split('《')[0].strip()
        num = choise.split('《')[-1].strip()
        num = changeData(num)
        return name, '<', num, data_list
    elif choise.upper() == 'Q':
        print('\033[34;1m谢谢使用！\033[0m')
        exit(-1)
    elif choise == '':
        #print('\033[31;1m请输入内容！\033[0m')
        return 'continue'
    else:
        name = choise.strip()
        return name, data_list


if __name__ == '__main__':
    data_list = getData()
    while True:
        args = checkArgs(data_list)
        stockFinder(args)
