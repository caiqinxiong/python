# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 商品名称 + 商品价格，如：
#         1 电脑 1999
#         2 鼠标 10
#         …
#         n 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，
# 则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 6. 用户输入Q或者q退出程序。
# 7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
goods = ['电脑','鼠标']
sale =[2000,10]
money = input('请输入充值金额>>>').strip()
shop_car = []#购物车
shop_car2 = []#存放订单详情
if money.isdigit():
    money = int(money)
    while True:
        print('''
        -----商品列表------
        序号 名称   售价
        0    %s     %d
        1    %s     %d
        n    购物车结算'''%(goods[0],sale[0],goods[1],sale[1]))
        user_choose = input('请输入想购买的商品序号>>>').strip()
        if user_choose.isdigit():
            user_choose = int(user_choose)
            if user_choose <= len(goods)-1:#判断输入序号在范围内
                if money>= sale[user_choose]:#判断余额是否足够
                    money -= sale[user_choose]  # 购买成功，减少余额
                    shop_car.append(goods[user_choose])
                    print('[%s]加入购物车成功,购物车列表有%s：'%(goods[user_choose],shop_car))
                else:
                    print('加入购物车失败：余额不足，当前可用余额为%s,购物车列表有%s：'%(money,shop_car))
                    user_choose2 = input('请输入"物品名称"删除购物车物品或输入"n"结算购物车>>>')
                    if user_choose2 in shop_car:
                        shop_car.remove(user_choose2)#移除用户输入的商品名称
                        money += sale[goods.index(user_choose2)]#增加减少商品的余额
                    elif user_choose2 == 'n':
                        if len(shop_car)>0:
                            print('---订单列表---')
                            for i in shop_car:
                                if i not in shop_car2:
                                    shop_car2.append(i + '*' + str(shop_car.count(i)))
                                else:
                                    pass
                            print(shop_car2)
                            print('余额为%s'%money)
                            break
                        else:
                            print('购物车为空！')
                            print('余额为%s' % money)
                            break
                    else:
                        print('输入错误，购物车无该商品!')
            elif user_choose > len(goods)-1 or user_choose < len(goods)-1:#判断输入序号在范围外
                print('商品序号不正确。请重新输入！！')
            elif user_choose == 'n':#用户结账
                if len(shop_car) > 0:
                    print('---订单列表---')
                    for i in shop_car:
                        if i not in shop_car2:
                            shop_car2.append(i + '*' + str(shop_car.count(i)))
                        else:
                            pass
                    print(shop_car2)
                    print('余额为%s' % money)
                else:
                    print('购物车为空！')
                    print('余额为%s' % money)
                    break
            elif user_choose == 'q':
                print('退出程序！')
                if len(shop_car) > 0:
                    print('---订单列表---')
                    for i in shop_car:
                        if i not in shop_car2:
                            shop_car2.append(i + '*' + str(shop_car.count(i)))
                        else:
                            pass
                    print(shop_car2)
                    print('余额为%s' % money)
                else:
                    print('购物车为空！')
                    print('余额为%s' % money)
                break
        elif user_choose == 'q':
            print('退出程序！')
            if len(shop_car) > 0:
                print('---订单列表---')
                for i in shop_car:
                    if i not in shop_car2:
                        shop_car2.append(i + '*' + str(shop_car.count(i)))
                    else:
                        pass
                print(shop_car2)
                print('余额为%s' % money)
            else:
                print('购物车为空！')
                print('余额为%s' % money)
            break
        elif user_choose == 'n':
            if len(shop_car) > 0:
                print('---订单列表---')
                for i in shop_car:
                    if i not in shop_car2:
                        shop_car2.append(i + '*' + str(shop_car.count(i)))
                    else:
                        pass
                print(shop_car2)
                print('余额为%s' % money)
                break
            else:
                print('购物车为空！')
                print('余额为%s' % money)
                break
        else:
            print('输入有误！')
            break
elif money == 'q':
    print('退出程序')
elif money == 'n':
    print('本次购物订单为空！')
else:
    print('输入有误！')



