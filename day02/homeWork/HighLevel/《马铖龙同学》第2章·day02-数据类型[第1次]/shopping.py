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

shopping_car = []
sum_amount = 0
amount = int(input("请输入你的充值金额:"))
sum_amount +=amount
payment = 0
print("你可以输入Q或者q结束，按n或者N进行结算")
print("你的总金额为:%s" %sum_amount)
print("--------------------------")
shopping_list = [{"电脑":1999},{"鼠标":10},{"iphone":6000},{"相机":13000}]
for index,value in enumerate(shopping_list):
    print(index+1,value)
print("-------------------------")
while True:
    choice= input("请输入你想选购的商品或者输入n结算:")
    if choice.isdigit():
        if int(choice) < len(shopping_list)+1:
            shopping_car.append(shopping_list[int(choice) - 1])
#            print(shopping_list[int(choice) - 1])
            print("你已经购买了%s" % (shopping_car))
        else:
            print("请重新输入正确的编号")
    else:
        if str(choice) == "Q" or str(choice) == 'q':
            shopping_list.clear()
            print("再见")
            break
        elif choice == "N" or choice == "n":
            for i in shopping_car: #循环购物车列表
                payment +=int(list(i.values())[0]) #购物车总钱数
            while payment > sum_amount: #比较总钱数和购物总价格
                for index1,value1 in enumerate(shopping_car):
                    print(index1+1,value1)

                del_shopping = int(input("商品总额大于你的钱数，请删除一些商品（序列号）:"))
#                print(sum_amount)
                print("购物总价格为:%s"%payment)
                payment -=(list(shopping_car[del_shopping - 1].values())[0]) #剩余购物总钱数
                shopping_car.pop(del_shopping - 1)
        break
print("你已购东西为：%s，剩余金额为:%s元" %(shopping_car, sum_amount - payment))




# if choice >= len(shopping_list)+1: #判断选择的序号是否在范围之内
#     if sum_amount > shopping_list[choice+1].values(): #判断钱是否大于商品价格
#         print(shopping_list[choice+1].index(),shopping_list[choice+1].index())
#         shopping_car.append(shopping_list[choice+1].keys()) #添加商品到购物车
#         sum_amount -=shopping_list[choice+1].values() #剩余钱数
#
#     else:
#         if len(shopping_car):
#             print(shopping_car)
#         else:
#             print("你没有足够的钱")
#ele




