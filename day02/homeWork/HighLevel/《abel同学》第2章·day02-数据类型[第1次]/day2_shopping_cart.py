#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 21:24
# @Author  : Abel
# @File    : day2_shopping_cart.py
# @Software: PyCharm

"""
作业需求:
1. 用户先给自己的账户充钱：比如先充3000元。
2. 页面显示 序号 + 商品名称 + 商品价格，如：
        1 电脑 1999
        2 鼠标 10
        …
        n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，
   若充值的钱数充足，则可以直接购买。
6. 用户输入Q或者q退出程序。
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
"""
# 初始化用户选购信息
shopping_info = {"balance": "Null", "trolley": [], "commodity_price": 0}
# 转换为变量，以便后期调用
balance = shopping_info["balance"]
commodity_price = shopping_info["commodity_price"]
trolley_commodity = shopping_info["trolley"]

# 初始化商城商品
commodity_dict = {"电脑": 8000, "鼠标": 299, "键盘": 499, "耳机": 1299, "移动硬盘": 599}

print("京东数码".center(80, "="))
status = "shopping"
while status != "Q":

    # 账户充值逻辑
    # 判断是否有余额,没有则进行充值,只能在充值一次.
    if balance == "Null":
        budget = input("请输入充值的金额! Q=退出>>>").strip()
        if budget.upper() == "Q":
            break
        if budget.isdigit():
            balance = int(budget)
        else:
            print("输入有误，请输入纯数字!")
            continue

    # 商品展示逻辑
    commodity_list = []
    print("商品展示".center(80, "="))
    for commodity in enumerate(commodity_dict):
        # 将商品字典内商品添加至商品列表,方便后期选择
        commodity_list.append(commodity)
        print("{}. {} {}".format(commodity[0], commodity[1], commodity_dict[commodity[1]]))
    else:

        # 商品选购逻辑
        choose = input("请输入序号[0-{}]选购商品, Q=退出>>>".format(len(commodity_list)-1)).strip()
        if choose.upper() == "Q":
            break
        if choose.isdigit():
            choose = int(choose)
        else:
            print("输入有误，请输入纯数字!")
            continue
        # 根据列表总长度判断输入是否为存在的商品
        if not choose < len(commodity_list):
            print("输入有误，并重新输入")
            continue
        chose_commodity = commodity_list[choose][1]
        price = commodity_dict[commodity_list[choose][1]]
        # 此处用tuple,以便集合去重
        trolley_commodity.append((chose_commodity, price))
        shopping = input("输入任意键继续购物, N=结算, Q=退出 >>>").strip().upper()
        if shopping == "Q":
            break
        if shopping != "N":
            continue
        # 循环,计算购物车内已选购商品的总价,并记录
        for i in trolley_commodity:
            commodity_price += i[1]

        # 账户余额大于等于购物车内已购商品总金额的情况下逻辑
        if balance >= commodity_price:
            # 余额减去已消费金额
            balance = balance - commodity_price
            print("结算成功".center(80, "="))
            print("离开商城...")
            status = "Q"
        # 账户余额小于购物车内已购商品总金额的情况下逻辑
        elif balance < commodity_price:
            # 购物车内物品删除逻辑
            print("购物车内".center(80, "="))
            while balance < commodity_price:
                print("余额不足,无法支付; 余额:{},商品费用{}".format(balance, commodity_price))
                for i in enumerate(trolley_commodity):
                    print("{}. {} {}".format(i[0], i[1][0], i[1][1]))
                del_commodity = input("请输入序号[0-{}]选择要删除的商品 Q=退出>>>".format(len(trolley_commodity)-1)).\
                    strip()
                if del_commodity.upper() == "Q":
                    break
                if del_commodity.isdigit():
                    del_commodity = int(del_commodity)
                else:
                    print("输入有误，请输入纯数字!")
                    continue
                # 根据列表总长度判断输入是否为购物车内商品
                if not del_commodity < len(trolley_commodity):
                    print("输入有误，并重新输入")
                    continue
                # 将已删除商品价格,从选购商品总额中减去
                commodity_price -= trolley_commodity[del_commodity][1]
                # 移除已选购商品
                trolley_commodity.pop(del_commodity)
            else:
                # 余额减去已消费金额
                balance = balance - commodity_price
                print("结算成功".center(80, "="))
                print("离开商城...")
                status = "Q"
else:
    print("谢谢惠顾，欢迎下次光临".center(80, "="))
    # 集合将列表内重复的商品名与价格去除
    commodity_sort = set(trolley_commodity)
    for i in commodity_sort:
        print("商品:{} ,价格 {}, 数量:{}".format(i[0], i[1], trolley_commodity.count(i)))
    print("此次消费:{},账户余额{}".format(commodity_price, balance))
