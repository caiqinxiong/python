#!/usr/bin/nev python

shopping_list = [
    {"name":"电脑","price":1999},
    {"name":"手机","price":3000},
    {"name":"汽车","price":300000}
]

shopping_cart = []

user_money = input("请充值:")
if user_money.isdigit():
    user_money = int(user_money)
    while True:
        for itme in shopping_list:
            print(shopping_list.index(itme),itme["name"],itme["price"])
        user_inupt = input("请输入的想要选择的商品序号:")
        if user_inupt.isdigit():
            user_inupt = int(user_inupt)
            if user_inupt < len(shopping_list) and user_inupt >= 0:
                p_itme = shopping_list[user_inupt]
                if p_itme["price"] <= user_money:
                    shopping_cart.append(p_itme)
                    user_money -= p_itme["price"]
                    print("余额%s" % user_money)
                else:
                    print("余额不足%s" % user_money)
            else:
                print("商品不存在")

        elif user_inupt.upper() == "Q":
            print("------- 购买的商品 ------")
            for p in shopping_cart:
                print(p["name"],p["price"])
            exit()
        elif user_inupt.upper() == "N":
            print("------- 购买的商品 ------")
            for p in shopping_cart:
                print(p["name"], p["price"])
            print("-------------------------")
        else:
            print("您输入的有误，请重新输入")
else:
    print("你的输入有误")





