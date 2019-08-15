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

shopping_list = [
    {'电脑':3000},
    {'鼠标': 70},
    {'手机': 1440},
    {'充电宝': 100},
    {'音响': 1000},
    {'耳机': 120},
    {'去购物车结算':''},
]
shopping_car = []
flag = True
while flag:
    money = input('请充值金额：')
    if money.isdigit():
        money = int(money)
        print('您的余额为：%s'% money)
        while flag:
            for i in shopping_list:
                for k in i:
                    print('%s.%s %s'% (shopping_list.index(i)+1,k,i.get(k)))
            chooise = input('请输入商品序号：').strip()
            if chooise.isdigit():
                chooise = int(chooise)
                if chooise > 0 and chooise < len(shopping_list):
                    print('%s已加入购物车'%shopping_list[chooise-1])
                    shopping_car.append(shopping_list[chooise-1])
                elif chooise == len(shopping_list):
                    while flag:
                        sum = 0
                        for w in shopping_car:
                            for k1 in w:
                                print('%s.%s %s' % (shopping_car.index(w) + 1, k1, w.get(k1)))
                                sum += int(w.get(k1))
                        if money >= sum:
                            overplus = money - sum
                            chooise1 = input('余额充足，请输入q确认购买，并退出').upper().strip()
                            if chooise1 == 'Q':
                                for w in shopping_car:
                                    for k1 in w:
                                        print('%s.%s %s' % (shopping_car.index(w) + 1, k1, w.get(k1)))
                                print('此次共消费%s账户余额%s'%(sum,overplus))
                                flag = False

                            else:print('请输入正确字符')
                        elif money < sum:
                            flag = True
                            sum1 = sum
                            while flag:
                                if money < sum1:
                                    overplus1 = sum1 - money
                                    print('余额不足，还差%s，请删除购物车中的部分商品'%overplus1)
                                    chooise2 = input('请输入要删除的商品编号：')
                                    if chooise2.isdigit():
                                        chooise2 = int(chooise2)
                                        if chooise2 > 0 and len(shopping_car) >= chooise2:
                                            shopping_car.pop(chooise2-1)
                                        else:print('请输入正确商品序号')
                                    else:print('请输入正确编号')
                                    sum1 = 0
                                    for x in shopping_car:
                                        for k2 in x:
                                            print('%s.%s %s' % (shopping_car.index(x) + 1, k2, x.get(k2)))
                                            sum1 += int(x.get(k2))
                                            overplus1 = sum1 - money
                                elif money >= sum1:
                                    overplus2 = money - sum1
                                    chooise2 = input('余额充足，请输入q确认购买，并退出').upper().strip()
                                    if chooise2 == 'Q':
                                        for w in shopping_car:
                                            for k1 in w:
                                                print('%s.%s %s' % (shopping_car.index(w) + 1, k1, w.get(k1)))
                                        print('此次共消费%s账户余额%s' % (sum1, overplus2))
                                        flag = False

                                    else:
                                        print('请输入正确字符')
                else:
                    print('请输入列表展示的商品序号')

            else:
                print('请输入正确的商品序号')
    else:
        print('输入有误，请输入数字')






