#Author:leesirc
#Function: 1,模糊匹配股票名称 2，允许按股票价格、涨跌幅、换手率这几列来筛选信息
#Date: 2019.7.25 v1

import re

with open("stock_data.txt",'r') as f_stock:
    f_list = [i.split() for i in f_stock]
# for i in f_list:
#     print(i)

#最新价、涨跌幅、换手率
def stock(enter_data,index):
    #判断输入格式是否正确
    if len(re.split(r'(?:[<>])',enter_data)) >= 2 and re.split(r'(?:[<>])',enter_data)[1].replace(".","").isdigit():
        num_ge = 0
        num_le = 0
        print(f_list[0])
        for m_list in f_list[1:]:
            if ">" in enter_data:
                if float(m_list[index].split("%")[0]) > float(enter_data.split(">")[1]):
                    num_ge += 1
                    print(m_list)
            elif "<" in enter_data:
                if float(m_list[index].split("%")[0]) < float(enter_data.split("<")[1]):
                    num_le += 1
                    print(m_list)

        if ">" in enter_data:
            print("\033[1m 您输入的【%s】共匹配 【%s】项" % (enter_data, num_ge))
        elif "<" in enter_data:
            print("\033[1m 您输入的【%s】共匹配 【%s】项" % (enter_data, num_le))
    else:
        print("\033[31m 您输入有误,后面不是数字，请正确输入，比如：%s > number or %s < number" %(enter_data,enter_data))





#模糊匹配股票名称
def stock_name(enter_data,index):
    num_stock_name = 0
    print(f_list[0])
    for m_list in f_list[1:]:
        if enter_data in m_list[2]:
            print(m_list)
            num_stock_name += 1
    if num_stock_name:
        print("\033[1m 您输入的 【%s】 共匹配 【%s】 项" %(enter_data,num_stock_name))
    else:
        print("\033[31m 您输入有误，没有类似的股票名称:%s" %enter_data)


def main():
    while True:
        enter_data = input("\033[34m 股票查询接口【q/Q退出】>>>: ").strip()
        if "最新价" in enter_data:
            # stock_latest_price(re.split(r'(?:[<>])',enter_data))
            stock(enter_data,4)
        elif "涨跌幅" in enter_data:
            stock(enter_data,5)
        elif "换手率" in enter_data:
            stock(enter_data,15)
        elif enter_data.upper() == "Q":
            print("\033[1m 程序即将正常退出")
            exit(0)
        else:
            stock_name(enter_data,2)


if __name__ == "__main__":
    main()