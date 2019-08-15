li=[
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':10},
    {'name':'键盘','price':50}
]

shooping_car = {}
shoop_money = 0

print("欢迎光临大铁锤水果店")
print("##################")

money = input("请进行充值：")

while 1:

    if int(money) > 0:
        #进行商品显示
        for I in li:
            print('序号:{} 商品:{} 价格:{}'.format((li.index(I) + 1), I['name'], I['price']))
        #进行商品选择
        choose = input('请选择你要购买的商品序号或者Q/q退出：')
        if choose.strip().isdigit() and int(choose) <= len(li):
            print(li[int(choose) - 1])

            choose_num = input('请输入购买商品的数量：')
            if choose_num.strip().isdigit():
                if int(money) >= li[int(choose) - 1]['price'] * int(choose_num):
                    money = int(money) - li[int(choose) - 1]['price'] * int(choose_num)  # 计算剩余的钱
                    shoop_money += li[int(choose) - 1]['price'] * int(choose_num)  # 消费的价格
                    shooping_car[li[int(choose) - 1]['name']] = int(choose_num)  # 把选中的商品增加到购物车

                    # 取购物车的商品和数量
                    for key, value in shooping_car.items():
                        # 通过购物车里面的商品得到对应于商品的价格
                        for I in li:
                            if I['name'] == key:
                                price = I['price']
                                print('你的购物车中商品有:{} 单价:{} ,数量为:{}'.format(key, price, value))
                    print('你的余额为：{}'.format(money))
                else:
                    print('余额不足，请重新选择商品')
                if int(money) == 0:
                    print("你已经没有钱了，无法再进行购物,请调整购物车或者再次充值")
            else:
                print('输入有误，数量为为整数，请重新输入')

        elif choose.upper() == 'Q':
            for key, value in shooping_car.items():
                for I in li:
                    if I['name'] == key:
                        price = I['price']
                        print('本次购买的商品有:{} 单价:{} ,数量为:{}'.format(key, price, value))
            print('你本次总共消费为：{}，你的余额为：{}'.format(shoop_money, money))
            exit(0)
        else:
            print('输入有误，序号为整数，请重新输入')


