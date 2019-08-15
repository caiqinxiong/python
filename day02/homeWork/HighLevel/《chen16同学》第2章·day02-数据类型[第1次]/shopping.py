# -*- coding:utf-8 -*-
# !/usr/bin/python

#设置变量
products = [['电脑', 1999], ['鼠标', 10], ['手机', 6888], ['衣服', 150], ['龙虾', 99]]
cart = []
shopping_money = 0
list = "商品列表"
list2 = "你已购买以下商品"
list3 = "购物车商品"

#循环商品列表
money = int(input("输入充值金额："))
while True:
    print(list.center(20, '-'))
    for index, i in enumerate(products):
        print("%s. %s   %s" % (index + 1, i[0], i[1]))
    print("%s. %s" % ('n', '购物车结算'))

    #实现添加商品到购物车
    choice = input("输入想买的商品：")
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(products):
            cart.append(products[choice - 1])
            print("商品 %s 已添加到购物车" % (products[choice - 1]))
            shopping_money += products[choice - 1][1]
        else:
            print("商品不存在")

    #购物车结算功能
    elif choice == 'n':
        if len(cart) > 0:
            while shopping_money > money:
                print(list3.center(20, '-'))
                for index, i in enumerate(cart):
                    print("%s. %s   %s" % (index + 1, i[0], i[1]))
                print("商品总额：%s 元 账户余额：%s 元" % (shopping_money, money))
                choose = int(input("余额不足以支付全部商品，请删除一些商品:"))
                if choose <= len(cart):
                    shopping_money -= cart[choose - 1][1]
                    del cart[choose - 1]
                else:
                    print("商品不存在")
            else:
                money -= shopping_money
                print(list2.center(20, '-'))
                for index, i in enumerate(cart):
                    print("%s. %s   %s" % (index + 1, i[0], i[1]))
                print("商品总额：%s 元 账户余额：%s 元" % (shopping_money, money))
                print('欢迎再次光临')
                break
        else:
            print("商品总额：%s 元 账户余额：%s 元" % (shopping_money, money))
            print('欢迎再次光临')
            exit()

    #直接退出不进行结算
    elif choice == 'q' or choice == 'Q':
        if len(cart) > 0:
            print(list3.center(20, '-'))
            for index, i in enumerate(cart):
                print("%s. %s   %s" % (index + 1, i[0], i[1]))
            print("未结算金额：%s 元  账户余额：%s 元 " % (shopping_money, money))
            break
        else:
            print("商品总额：%s 元  账户余额：%s 元" % (shopping_money, money))
            print('欢迎再次光临')
            exit()