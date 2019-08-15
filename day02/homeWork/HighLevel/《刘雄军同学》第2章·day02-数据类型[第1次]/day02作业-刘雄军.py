# 作业题目: 购物车
# 作业需求:
# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 商品名称 + 商品价格，如：
#         1 电脑 1999
#         2 鼠标 10
#         …
#         n 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 6. 用户输入Q或者q退出程序。
# 7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。

goods = [{"name": "电脑", "price": 1999},
          {"name": "鼠标", "price": 10},
          {"name": "电源", "price": 20},
          {"name": "手机", "price": 998}, ]
shopping_car = {}
shopping_count = {}
for i in range(len(goods)):
    shopping_count.setdefault(goods[i]['name'], 0)
money_input = int(input('请输入你要充值的金额:').strip())
Flag = True
while Flag:
    print('序号   商品名称   商品价格')
    for count_i in goods:
        print(goods.index(count_i) + 1,count_i['name'],count_i['price'])
    user_input = input('输入商品序号：\n(输入Q或者q退出程序): \n(输入n结账): ').strip()
    if user_input.isdigit():
        user_input = int(user_input)
        if 0 < user_input <= len(goods):
            print(goods[user_input - 1]['name'], goods[user_input - 1]['price'])
            shopping_car[goods[user_input - 1]['name']] = goods[user_input - 1]['price']
            for key in shopping_car.keys():
                if key in goods[user_input - 1]['name']:
                    shopping_count[key] += 1
            print(shopping_car)
            print(shopping_count)
        else:
            print('Sorry！您输入数字不在规定范围内，请重新输入！')
    elif user_input == 'Q' or user_input == 'q':
        print('谢谢光临！')
        Flag = False
    elif user_input == 'n':
        total_value = 0
        for key_1 in shopping_car.keys():
            for key_2 in shopping_count.keys():
                if key_1 == key_2:
                    total_value = total_value + shopping_count[key_2] * shopping_car[key_1]
        print('total_value = ', total_value)
        while total_value > money_input:
            total_value = 0
            user_input_again = input('请删除商品，(1：电脑，2：鼠标，3：电源，4：手机，)')
            user_input_again = int(user_input_again)
            print('---------------------------------------------------------------------')
            for key in shopping_car.keys():
                if key == goods[user_input_again - 1]['name']:
                    if shopping_count[key] == 0:
                        shopping_count[key] = shopping_count[key]
                    else:
                        shopping_count[key] -= 1
                    print('商品数量：', shopping_count)
                    for key_1 in shopping_car.keys():
                        for key_2 in shopping_count.keys():
                            if key_1 == key_2:
                                total_value = total_value + shopping_count[key_2] * shopping_car[key_1]
                    print('购物车剩余物品价值：', total_value, '元')
                    print('---------------------------------------------------------------------')
        print('---------------------------------------------------------------------')
        print('此次用户购买的商品，数量，单价共计：')
        print(shopping_car)
        print(shopping_count)
        print('此次购买商品共消费：%s 元，且账户余额共计：%s 元' % (total_value, money_input - total_value))
        print('---------------------------------------------------------------------')
        Flag = False
    else:
        print('输入的不是数字，请重新输入!')