#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#商品清单
commoditys= [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "键盘", "price": 20},
         {"name": "耳机", "price": 50},
         ]
#购买的商品
things = {}
#初始金额
money = 0
while True:
    add_money = input('请输入需要充值的钱数：').strip()
    if add_money.isdigit():
        money += int(add_money)
        print('您已成功充值%s元' % add_money)
        break
    else:
        print('您输入了非法字符，请重新输入：')
#标准位
flag = True
while flag:
    x = 0
    print('有如下商品供您选择：')
    while x < len(commoditys):
        print(x, end='\t')
        for y  in commoditys[x].values():
            print(y,end='\t')
        print("")
        x+=1
    print('输入N或n进行结算')
	#去除用户输入时带入的一些空格和换行符，制表符
    select_num = input('请输入您的选择：').strip()
	#判断输入的是否是数字
    if select_num.isdigit():
        select_num = int(select_num)
        if 0 <= select_num < len(commoditys):
            #通过字典来存储每个商品的名称价格数量。
            if (select_num ) not in things:
                things[select_num] = {'name': commoditys[select_num]['name'], 'price': commoditys[select_num]['price'], 'sum': 1}
            else:
                things[select_num]['sum'] += 1
            print('您选择的商品名称为：{}商品价格：{}商品数量：1，成功添加到购物车中。' \
                  .format(things[select_num]['name'], things[select_num]['price']))
        else:
            print('您输入的序号超出范围，请重新输入：')
	#将用户输入的大小写字母都转化成小写并进行判断
    elif select_num.lower() == 'n':
        while True:
            print('您购物车的有以下商品：')
            total_price = 0
            for id, information_dict in things.items():
                total_price += information_dict['price'] * information_dict['sum']
                print('序号：{}商品名称:{}商品单价:{}此商品总价：{}' .format(id, information_dict['name'],\
                            information_dict['price'], information_dict['price'] * information_dict['sum'] ))
            print('您购买的商品一共：%s元' % total_price)

            if money >= total_price:
                money -= int(total_price)
                print('您已成功购买以上所有商品，余额为%s元，期待您的下次光临哟~' % money)
                flag = False
                break
            else:
				#金额不满足现有的金额时候进行删除商品，通过将对应商品的sum键的值进行减法。
                print('余额不足，还差%s元，请删掉一些商品' % (total_price - money))
				#去除用户输入时带入的一些空格和换行符，制表符
                del_num = input('请输入要删除的商品序号：').strip()
				#判断输入的是否是数字
                if del_num.isdigit():
                    del_num = int(del_num)
                    if (del_num ) in things:
                        things[del_num]['sum'] -= 1
                        if not things[del_num]['sum']:
                            del things[del_num]
                    else:
                        print('您输入的序号超出范围，请重新输入：')
                else:
                    print('您输入了非数字元素，请重新输入：')
    elif select_num.upper() == 'N':
        print('欢迎再来')
    else:
        print('您输入的选项不存在。请重新输入:')