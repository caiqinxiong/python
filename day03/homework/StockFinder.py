# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/21 下午10:30
def getData():
    '''获取数据'''
    stock_data_list = []
    with open(r'stock_data.txt',mode='r',encoding='utf-8') as f:
        for line in f:
             line = line.strip()
             if line:
                 #print(line.split())
                 print('|'.join(line.split()))
                 stock_data_list.append(line.split())
        print('~'*100)
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
        return float(data)
    return data

def printList(listData):
    '''打印列表'''
    print('一共搜索到\033[31;1m%s\033[0m条结果，详情如下：' % len(listData))
    print('~'*100)
    print('|'.join(data_list[0]))
    for i in listData:
        print('|'.join(i))
    print('~'*100)

def compareData(compare,num,index,data_list):
    '''比较查询'''
    num_list = []
    # 获取比较完成数据，添加到列表里
    for i in range(1,len(data_list)):
        if compare == '<':
            if  changeData(data_list[i][int(index)]) < float(num):
                num_list.append(data_list[i])
        else:
            if changeData(data_list[i][int(index)]) > float(num):
                num_list.append(data_list[i])
    # 打印比较结果
    printList(num_list)


def stockFinder(*args):
    '''比较查找数据'''
    name = args[0]
    data_list = args[-1]
    try:
        compare = args[1] # 比较符号
        num = args[2] # 比较数据
        # 获取输入项名称，支持模糊查找
        for i in data_list[0]:
            if not i.find(name) < 0:
                index = data_list[0].index(i) # 获取该名称对应的index值
                compareData(compare,num,index,data_list)
            else:
                print('输入有误！')
    except:
        find_data = []
        # 模糊查找
        for i in range(1,len(data_list)):
            if not data_list[i][2].find(name) < 0:
                find_data.append(data_list[i])
            else:
               print('无查询结果！')
        # 打印查找结果
        printList(find_data)

def checkArgs():
    '''校验传入参数'''
    choise = input('股票查询接口>>:')
    if not choise.find('>') < 0:
        name = choise.split('>')[0].strip()
        num = choise.split('>')[-1].strip()
        return name,'>',num
    elif not choise.find('<') < 0:
        name = choise.split('<')[0].strip()
        num = choise.split('<')[-1].strip()
        return name,'<',num
    else:
        name = choise.strip()
    return name

if __name__ == '__main__':
    # data_list = getData()
    # stockFinder('成交量','>','100000',data_list)
    # print('欢迎来到股票查询系统！')
    data_list = getData()
    #while True:
    #aa = checkArgs()
    print(data_list[0])