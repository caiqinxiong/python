# 作业需求：购物车
'''
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
'''
#商品列表
products = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "键盘", "price": 20},
         {"name": "音响", "price": 998},
         ]
products_car = {}
while 1:
    money = input('请输入充值的钱数：').strip()
    if money.isdigit():
        money = int(money)
        print('您已成功充值%s元' % money)
        break
    else:
        print('您输入了非法字符，请重新输入：')
flag = True
while flag:
    print('有如下商品供您选择：')
    for index, commodity_dict in enumerate(products):
        print('{}\t{}\t{}'.format(index + 1, commodity_dict['name'], commodity_dict['price']))
    print('输入n进行结算\n输入Q或q退出程序(如不结算购物车可直接退出)')
    select_num = input('请输入您的选择：').strip()
    if select_num.isdigit():
        select_num = int(select_num)
        if 0 < select_num <= len(products):
            if (select_num - 1) not in products_car:
                products_car[select_num - 1] = { \
                    'name': products[select_num - 1]['name'], 'price': products[select_num - 1]['price'], 'amount': 1}
            else:
                products_car[select_num - 1]['amount'] += 1
            print('您选择的商品具体信息：商品名称：{}商品价格：{}商品数量：1，并成功添加到购物车中。' \
                  .format(products[select_num - 1]['name'], products[select_num - 1]['price']))
        else:
            print('您输入的序号超出范围，请重新输入：')
    elif select_num.upper() == 'N':
        while 1:
            print('您购物车的具体商品如下：')
            total_price = 0
            for ind, com_dict in products_car.items():
                print('序号：{}商品名称{}商品单价{}此商品总价：{}' \
                      .format(ind + 1, com_dict['name'], com_dict['price'], com_dict['price'] * com_dict['amount']))
                total_price += com_dict['price'] * com_dict['amount']
            print('————————> 总价格：%s元' % total_price)

            if money >= total_price:
                money = int(money)
                print('您已成功购买以上所有商品，余额为%s元，期待您的下次光临哟~' % money)
                flag = False
                break
            else:
                print('余额不足，还差%s元，请忍痛割爱，删掉一些商品' % (total_price - money))
                del_num = input('请输入要删除的商品序号：').strip()
                if del_num.isdigit():
                    del_num = int(del_num)
                    if (del_num - 1) in products_car:
                        products_car[del_num - 1]['amount'] -= 1
                        if not products_car[del_num - 1]['amount']:
                            del products_car[del_num - 1]
                    else:
                        print('输入有误，请重新输入：')
                else:
                    print('您输入了非数字元素，请重新输入：')
    elif select_num.upper() == 'Q':
        print('欢迎下次光临哟')
    else:
        print('您输入的选项不存在。请重新输入:')