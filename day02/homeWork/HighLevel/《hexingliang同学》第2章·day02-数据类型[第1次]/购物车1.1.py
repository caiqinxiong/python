#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 定义购物车商品合计价格
total = 0

# 购物清单
shopping_list = []

# 可选商品信息
commodity_list = [
    ('电脑', '1999'),('鼠标', '10'),
    ('显示器', '666'),('键盘', '50'),('电源排插', '60')
]

balance = input(">>>请您输入您要充值的金额:")
while True:
    # 判断输入金额为数字组合，如果不是合法数字，提示重新输入
    # 这里有个坑，input和isdigit()函数，如果input输入的是纯数字，这里input的是int型，我记得老师说过input的都是字符串
    balance = str(balance)
    if balance.isdigit():
        print ('>>>您的金额为：' ,int(balance))
        print ()
        print ('----------商品信息----------')

        # 打印可选商品信息
        for shopping_name,price in enumerate(commodity_list):
            print (shopping_name, price)

        choice = input('\n请选择您要购买的商品,输入n结算,q为退出：')
        # 对用户输入商品序号判断范围
        if choice.isdigit() and int(choice) < len(commodity_list):
            # 确定用户选择的商品
            shopping = commodity_list[int(choice)]
            # 获取用户选择商品和价格，并计算购物车中所选商品的合计价格
            price_cout = int(shopping[1])
            total = total + price_cout
            shopping_list.append(shopping)
            print ('>>>购物车的商品：' ,shopping_list)
            print ('>>>合计：',total, '元!')
        # 用户进行购物车商品的结算，购物成功或失败退出程序
        elif choice == 'n' or choice == 'N':
            balance = int(balance)
            if balance >= total:
                balance -= total
                print ('>>>购物成功,您的余额为：', balance, '元!')
                print ('>>>已结算商品：', shopping_list)
                break
            # 如果用户余额不足，则提示用户移除购物车里面的一些商品，再进行结算
            else:
                print ('>>>余额不足,购买商品失败,请移除一些商品！')
                for shopping_name, price in enumerate(shopping_list):
                    print(shopping_name, price)
                choice = input('\n请选择您要移除的商品,q为退出：')
                if choice.isdigit() and int(choice) < len(shopping_list):
                    shopping = shopping_list[int(choice)]
                    price_cout = int(shopping[1])
                    total = total - price_cout
                    del shopping_list[int(choice)]
                    print('>>>合计：',total, '元!')
                    print (shopping_list)
        # 用户取消购物，退出程序
        elif choice == 'q' or choice == 'Q':
            print ('>>>购物取消!此次消费 0 元,余额为：', balance, '元!')
            print ('>>>未结算的商品：', shopping_list)
            break
        else:
            print ('>>>输入商品序号有误，请重新输入!')
    else:
        balance = input(">>>充值失败,请输入合法金额(整数):")
