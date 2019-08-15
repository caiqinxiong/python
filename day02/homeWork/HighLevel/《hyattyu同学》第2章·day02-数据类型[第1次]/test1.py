#!/usr/bin/python
# -*- coding: UTF-8 -*-
money = int(input("请输入充值金额").strip())
#money=10000;
item_list = [
    {"name":"iphone4" ,"price":1000},
		{"name":"iphone5" ,"price":2000},
		{"name":"iphone6" ,"price":3000},
		{"name":"iphone7" ,"price":4000},
		{"name":"iphone8" ,"price":5000},
		{"name":"iphoneX" ,"price":6000}
	]
i = 0
for item in item_list:
    print("编号：{} 商品：{} 价格：{}".format(i,item["name"],item["price"]))
    i+=1
shopping_list = {}
sum_price = 0
balance = money
while True:
    item_number = int(input("请输入要购买的商品编号").strip())
    if item_number>len(item_list)-1:
        print("输入错误，请重新输入")
        continue
    if int(item_list[item_number]["price"])<balance:
        shopping_list[item_list[item_number]["name"]]=item_list[item_number]["price"]
        sum_price = sum_price+int(item_list[item_number]["price"])
        balance = money-sum_price
        print("购物车商品{}".format(shopping_list))
        print("余额{}".format(balance))
        quit=input("是否继续购物Y/Q")
        if quit.upper()=="Q":
            for shoppingitem in shopping_list:
                print("商品 {} 价格 {}".format(shoppingitem,shopping_list[shoppingitem]))
            break
    else:
         print("余额不足")
         quit = input("是否继续购物Y/Q")
         if quit.upper() == "Q":
             for shoppingitem in shopping_list:
                 print("商品{} 价格 {}".format(shoppingitem, shopping_list[shopping_item]))
             break

         while True:
             delet_item = int(input("请选择要删除的商品").strip())
             flag = False
             for shopping_item in shopping_list:
                 if item_list[delet_item]["name"]==shopping_item:
                     del shopping_list[shopping_item]
                     print("删除成功")
                     flag = True
                     break
                 else:
                    print("商品不在购物车")
             if flag:
                 break
         print("购物车商品{}".format(shopping_list))
         balance = balance + int(item_list[item_number]["price"])
         sum_price  = sum_price - int(item_list[item_number]["price"])