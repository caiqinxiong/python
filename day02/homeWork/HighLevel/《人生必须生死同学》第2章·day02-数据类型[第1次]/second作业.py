#: @author: Tiga
#: @Time:   2018/8/22 14:11
#: @Email:  137534976@qq.com

user_input_money = int(input('请充值: '))

flag = True
# 标记用户的行为，如果为True则为购买，False为删除商品
action = True

# 商品信息
commodity_info = {
    '1': {'product_name':'电脑', 'price': 1999},
    '2': {'product_name':'鼠标', 'price': 10},
    '3': {'product_name':'键盘', 'price': 20},
    '4': {'product_name':'显示器', 'price': 888},
}




# 首页显示
msg = '''\
序号       商品名称            价格
1    {product_name1:^18}     {price1:^6}
2    {product_name2:^18}     {price2:^6}
3    {product_name3:^18}     {price3:^6}
4    {product_name4:^18}     {price4:^6}
n          购物车结算
q          退出程序
'''.format(product_name1=commodity_info['1']['product_name'],
           price1=commodity_info['1']['price'],
           product_name2=commodity_info['2']['product_name'],
           price2=commodity_info['2']['price'],
           product_name3=commodity_info['3']['product_name'],
           price3=commodity_info['3']['price'],
           product_name4=commodity_info['4']['product_name'],
           price4=commodity_info['4']['price'],

       )

# 用户购物车
shopping_cart = {}



print(msg)

while flag:
    # 用户购物车内商品总价值
    total_price = 0


    user_input = input('请选择商品: ')

    # 如果action不为True,进入删除商品的操作
    if not action:
        # 用户购物车内商品总价值
        total_price = 0

        if user_input in shopping_cart:
            shopping_cart[user_input]['count'] -= 1
            print('已删除一个: %s ' % shopping_cart[user_input]['product_name'])

            # 计算当前购物车单件商品总价格
            shopping_cart[user_input]['price'] = shopping_cart[user_input]['count'] * commodity_info[user_input]['price']


            # 如果商品数量等于0，则从购物车中删除
            if shopping_cart[user_input]['count'] == 0:
                del shopping_cart[user_input]



            # 显示当前购物车内物品
            print('当前购物车内物品: ')
            for i in shopping_cart:
                print('商品名称: {product_name:^8}\
                商品数量: {count:^2}\
                商品单价: {com_price:^8}\
                合计: {shop_price:^8}'.format(product_name=commodity_info[i]['product_name'],
                                            count=shopping_cart[i]['count'],
                                            com_price=commodity_info[i]['price'],
                                            shop_price=shopping_cart[i]['price']
                                            ))

        elif user_input == 'q':
            print('正在退出...')
            break


        else:
            print('你并没有添加该商品至购物车，请重新选择')



        # 计算用户删除商品后的购物车内总价格
        for i in shopping_cart:
            total_price += shopping_cart[i]['price']

        if total_price > user_input_money:
            continue
        else:
            print('当前充值金额为: %s, 已满足付款条件，可继续选择商品加入购物车或付款'% user_input_money)
            action = True
        print('总价格: %s'% total_price)


        continue


    if user_input.upper() == 'Q':
        print('正在退出...')
        flag = False
        break

    # 如果用户输入n，则进入结算页面
    if user_input == 'n':
        # 输出用户购物车里的商品
        if not len(shopping_cart):
            print('你没有购买商品')
            continue

        # 计算购物车内所有商品总价
        for i in shopping_cart:
            total_price += shopping_cart[i]['price']


        # 账户余额
        account_balance = user_input_money - total_price


        # 输出用户购买的商品、数量、单价
        print('本次购买商品清单:  ')
        for i in shopping_cart:
            print('商品名称: {product_name:^8}\
            商品数量: {count:^2}\
            商品单价: {com_price:^8}\
            合计: {shop_price:^8}'.format (product_name=commodity_info[i]['product_name'],
                                            count=shopping_cart[i]['count'],
                                            com_price=commodity_info[i]['price'],
                                            shop_price=shopping_cart[i]['price']
                                                 ))
        print('本次共消费: %s, 账户余额: %s' % (total_price, account_balance))
        break



    if user_input in commodity_info:
        # 用户购物车内商品总价值
        total_price = 0

        # 如果用户购物车里已经有该商品了，直接计算商品数量和但种类商品总价
        if user_input in shopping_cart:
            shopping_cart[user_input]['count'] += 1
            shopping_cart[user_input]['price'] = shopping_cart[user_input]['count'] * commodity_info[user_input]['price']


        # 将用户选择的商品添加至购物车
        else:
            shopping_cart[user_input] = {}
            shopping_cart[user_input].setdefault('product_name', commodity_info[user_input]['product_name'])
            shopping_cart[user_input].setdefault('price', commodity_info[user_input]['price'])
            shopping_cart[user_input]['count'] = 1


        # 输出用户选择的商品名称及价格
        print('当前选择商品:  序号:%s  商品名称:%s   价格:%s' % (user_input,
                                                            commodity_info[user_input]['product_name'],
                                                            commodity_info[user_input]['price']
                                                            ))

        # 输出用户购物车信息
        print('当前购物车内商品:  ')
        for i in shopping_cart:
            print('商品名称: {product_name:^12}\
            商品数量: {count:^4}\
            商品单价: {com_price:^6}\
            合计: {shop_price:^6}'.format (product_name=commodity_info[i]['product_name'],
                                            count=shopping_cart[i]['count'],
                                            com_price=commodity_info[i]['price'],
                                            shop_price=shopping_cart[i]['price']
                                                 ))



    else:
        print('输入有误，请重新输入!')


    # 计算购物车内所有商品总价
    for i in shopping_cart:
        total_price += shopping_cart[i]['price']

    print('总价格:', total_price)

    if total_price > user_input_money:
        print('当前充值金额为: %s ,充值金额不足以购买购物车内商品，请删除商品' % user_input_money)
        action = False











