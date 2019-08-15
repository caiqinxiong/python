product_list = [
    ['电脑',1999],
    ['键盘',200],
    ['结算','']
]
product_item = []
shopping_car = []
username = 'jimmy'
password = '123abc'

while True:
    user = input('请输入你的用户名：')
    if user == username :
        pdw = input('请输入你的密码：')
        if pdw == password :
            print('欢迎来到jimmy店！')
            while True:
                money = input('请输入您的充值金额：')
                if not money.isdigit():
                    print('输入有误，请确认输入的数字。')
                else:
                    money = int(money)
                    break
            while True:
                print('请选择你喜欢的商品：')
                for index,i in enumerate(product_list) :    #打印商品列表
                    print(index,i[0],i[1])            #打印商品列表
                choice = input('请输入你要购买商品序号，或者输入q或Q退出jimmy的店。').strip()
                if len(choice) == 0 :
                    print('还没有选择商品！')
                if choice.isdigit():       #判断输入是否是数字
                    choice = int(choice)
                    quit = int(len(product_list) - 1)
                    if choice < quit and choice >= 0 :
                        sum = int(input('输入数量'))
                        product_item = product_list[choice]   #选择的单一商品和单价
                        product_item.append(sum)        #选择的单一商品、单价加购买数量
                        shopping_car.append(product_item)   #将单一商品加入购物车
                    elif choice == quit:
                        for i in shopping_car:
                            print('您已经购买的商品：')
                            print('商品', '单价', '购买数量')
                            print(i[0], i[1], i[2])
                            toltal = int(i[1] * i[2])
                            print(toltal)
                        if toltal < money:
                             print('购买成功')
                             exit()
                        else:
                            print('余额不足，请重新选择！')
                            shopping_car.clear()
                            # break
                    else:
                        print('没有此商品，请重新选择！')
                elif choice == 'q' or 'Q':
                    if len(shopping_car):
                        for i in shopping_car:
                            print('您已经购买的商品：')
                            print('商品', '单价', '购买数量')
                            print(i[0], i[1], i[2])
                            toltal = int(i[1] * i[2])
                            exit()
                    else:
                        print('余额不足，没有成功购买商品！')
                        exit()
        else:
            print('密码错误，请重新输入！')
    else:
        print('用户名不正确，请重新输入！')