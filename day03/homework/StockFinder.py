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
    #print(stock_data_list[0][0])
    return stock_data_list


def compareData():
    '''比较查找数据'''
    data = getData()
    for i,j in enumerate(data):
        print(j)

if __name__ == '__main__':
    compareData()