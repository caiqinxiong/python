#!/usr/bin/python
# -*- coding:utf-8 -*-
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
while True:
    recharge=input('请输入充值金额：').strip()
    if recharge.isdigit():
        print('充值成功，您当前成功充值%s元' %recharge)
        break
    else:
        print('您输入了非法字符，请重新输入')
goods=[{"name":"电脑","price":1999},{"name":"鼠标","price":10},{"name":"键盘","price":100}]
print('*************商品列表展示******************')
for i  in  goods:
    print((goods.index(i))+1,i.get('name'),i.get('price'))
print('*******************************************')
print('(输入n为购物车结算,\n输入Q或者q退出程序)')
#定义购物车goods_car
goods_car={}
#定义总消费金额car_price
car_price=0
while True:
    select_number=input('请输入选择的商品序号：').strip()
    if  select_number.isdigit():
        if 0<int(select_number)<=len(goods):
            print("当前商品名称%s,商品价格%d" % (goods[int(select_number)-1].get('name'),goods[int(select_number)-1].get('price')))
            if (int(select_number)-1) not in goods_car:
                goods_car[int(select_number)-1]={"name":goods[int(select_number)-1].get('name'),"price":goods[int(select_number)-1].get('price'),"amount":1}
            else:
                goods_car[int(select_number) - 1]['amount']+=1
        else:
            print('您当前输入有误，请重新输入')
    elif select_number == 'n':
        while True:
            if goods_car=={}:
                print('当前购物车为空，无法结算，请进行购物')
            else:
                for i  in goods_car:
                    print(goods_car[i].get('name'),goods_car[i].get('amount'),goods_car[i].get('price'))
                    car_price+=goods_car[i].get('amount')*goods_car[i].get('price')
                if int(recharge)<car_price:
                    print('购物车中结算金额为%d,当前余额为%d,余额不足，请选择删除某商品' %(car_price,int(recharge)))
                    car_price=0
                    delete_number=input('请输入需要删除的商品的商品序号：').strip()
                    if delete_number.isdigit():
                        if 0<int(delete_number)<=len(goods_car):
                            goods_car[int(delete_number) - 1]['amount']-=1
                            if goods_car[int(delete_number) - 1]['amount']==0:
                                del goods_car[int(delete_number) - 1]
                        else:
                            print('您当前输入有误，请重新输入')
                    else:
                        print('您当前输入有误，请重新输入')
                else:
                    break
        print('当前用户成功消费%d元,余额为%d元' %(car_price,int(recharge)-car_price))
    elif select_number.upper()=='Q':
        print('成功退出')
        break
    else:
        print('您当前输入有误，请重新输入')
for j  in goods_car:
    print('购买的商品%s,数量%d,单价%d，\n此次共消费%d，\n账户余额%d' % (goods_car[j].get('name'),goods_car[j].get('amount'),goods_car[j].get('price'),
        car_price,int(recharge)-car_price))
