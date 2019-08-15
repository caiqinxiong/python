#!/usr/bin/env python
# coding: utf-8

"""
Created by zwb on 2018/8/19
"""
import sys

msg_dic = {
    "1": ["电脑", 1999],
    "2": ["鼠标", 50],
    "3": ["键盘", 500],
    "4": ["手机", 2000],
    "5": ["手机壳", 20]
}

#生成msg信息
msg = "商品清单如下: \n"
for k in msg_dic:
    sn = k
    goods = msg_dic[k][0]
    price = msg_dic[k][1]
    msg += "{0} {1} {2}\n".format(sn, goods, price)

account_balance = 0  #账户初始余额
total = 0 #总消费
shopping_cart = {} #购物车
while True:
    recharge = int(input("您充值的金额："))  #充值金额
    account_balance += recharge  #账户余额
    print("您的账户余额：{0}".format(account_balance))
    instructions = input("您是否继续充值，继续充值请输入y|Y \n开始购买商品请输入n|N \n退出请输入q|Q：")
    if instructions == "y" or instructions == "Y":
        continue
    elif instructions == "n" or instructions == "N":
        print(msg)
    elif instructions == "q" or instructions == "Q":
        print("欢迎下次光临, 再见！")
        break
    while True:
        num = input("退出请输入q|Q\n结算清输入n|N\n请输入您需要购买商品id：")
        if num == "q" or num == "Q":
            print("欢迎下次光临, 再见！")
            sys.exit()
        elif num == "n":
            while True:
                shopping_cart_msg = "\n商品id\t\t商品名称\t\t商品价格\t\t商品数量\t\t本商品总价\n"
                for k in shopping_cart:
                    shopping_cart_msg += "{0}\t\t\t{1}\t\t\t{2}\t\t\t{" \
                                         "3}\t\t\t{4}\n".format(k,
                                                              shopping_cart[
                                                                  k][0],
                                                              shopping_cart[
                                                                  k][1],
                                                                  shopping_cart[k][2], shopping_cart[k][3])
                print("您的购物车商品清单: {0}\n\n".format(shopping_cart_msg))
                if total > account_balance:
                    print("您的账户余额不足，请删除商品再进行结算")
                    rm = input("请输入您删除的商品id：")
                    if shopping_cart[rm][2] > 1:
                        shopping_cart[rm][2] -= 1
                        print(shopping_cart[rm][1])
                        total -= shopping_cart[rm][1]
                        shopping_cart[rm][3] -= shopping_cart[rm][1]
                    else:
                        total -= shopping_cart[rm][1]
                        shopping_cart.pop(rm)
                    continue
                else:
                    print("商品购买成功")
                    shopping_cart_msg += "\n本次共消费: {0}元，您的账户余额: {1}".format(
                        total, account_balance-total)
                    print(shopping_cart_msg)
                    print("欢迎下次光临, 再见！")
                    sys.exit()


        else:
            if num not in msg_dic:
                print("您输入的商品id有误，请重新输入")
                continue
            elif num not in shopping_cart:
                shopping_cart[num] = [msg_dic[num][0], msg_dic[num][1], 1,
                                      msg_dic[num][1]]
            else:
                shopping_cart[num][2] += 1
                shopping_cart[num][3] += msg_dic[num][1]
            total += msg_dic[num][1]
            print("您本次购买的商品信息: {0} {1} {2}".format(num, msg_dic[num][0],
                                                  msg_dic[num][1]))
            continue

