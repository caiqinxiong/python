'''
    1. 用户先给自己的账户充钱：比如先充3000元。
    2. 页面显示 序号 + 商品名称 + 商品价格，如：
            1 电脑 1999 
            2 鼠标 10
            …
            n 购物车结算
    3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
    4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
    6. 用户输入Q或者q退出程序。
    7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
'''

goods =[
    {"name":"电脑", "price": 1999},
    {"name":"鼠标", "price": 10},
    {"name":"游艇", "price": 20},
    {"name":"美女", "price": 998},
    {"name":"手机", "price": 2699}
]
info = '''
------购物指南------
0.输入q或者Q可退出购物！
1.输入n结算购物！
2.输入l查看购物车内容！
注意：未结算不会自动结算哦！
'''
print(info)
shopping_list = []
shoppint_car = []
salary = input('请输入存款:')

if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(goods):
            print(index,item)
        user_choice = input("选择要买的商品>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(goods) and user_choice >= 0:
                p_item = goods[user_choice]
                shoppint_car.append(p_item)
                print("添加 %s 到购物车成功"%p_item['name'])
            else:
                print("商品[%s]不存在"%user_choice)
        elif user_choice == 'n':
            total = 0
            for index,item in enumerate(shoppint_car):
                print(index,item)
                total += int(item['price'])
            if total <= salary:
                salary = salary - total
                shopping_list += shoppint_car
                print('购买成功！余额%s' % salary)
            else:
                print("你的钱只剩[%s]la ,买不起啦,输入d+序号可删除购物车内商品，如：d0" % salary)
        elif user_choice.startswith('d'):
            num = user_choice[1:]
            if num.isdigit():
                num = int(num)
                if num >= 0 and num < len(shoppint_car):
                    shoppint_car.pop(num)
                else:
                    print('没有该商品！请重新输入d+序号删除购物车内商品，如：d0')
        elif user_choice == 'l' or user_choice == 'L':
            print("----------- shopping car -----------")
            for index,item in enumerate(shoppint_car):
                print(index,item)
            print("----------- end -----------")
        elif user_choice == 'q' or user_choice == 'Q':
            print("----------- shopping list -----------")
            for index,item in enumerate(shopping_list):
                print(index,item)
            print('您的余额为%s'%salary)
            exit()
        else:
            print("exit")
            exit()