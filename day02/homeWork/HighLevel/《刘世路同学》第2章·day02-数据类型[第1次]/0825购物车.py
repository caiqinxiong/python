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

goods_list = {1 : ['电脑',1999], 2 : ['鼠标',10], 3 : ['键盘',299], 'n' : '购物车结算'}#网站售卖的商品及价格
user_account_balance = 0#用户的初始账户余额

user_name_password = {'liusl' : '123456','leiwen' : '987654'}#用户的账号和密码
user_login_max_times = 3#用户尝试登录的最大次数
user_login_status = 0#用户的登录状态

#用户登录模块
user_login_times = 0
while user_login_times <= 3:
    user_name = input('请输入用户名：')
    user_passwword = input('请输入密码：')
    if user_name in user_name_password:
        if user_passwword == user_name_password[user_name]:
            print('登录成功\n')
            user_login_status = 1#登录成功，修改用户的登录状态
            break
        else:
            print('用户名或密码输入错误，请重新输入')
            user_login_times +=1
            continue
    else:
        print('用户名或密码输入错误，请重新输入')
        user_login_times += 1
        continue
else:
    print('输入次数已超出，账号已锁定，请24小时后再尝试')


#显示网站正在出售的商品

print('本店售卖以下商品，请选购：\n')

for key in goods_list.keys():
    if key == 'n':
        continue
    else:
        print('', key, ' ', goods_list[key][0], '      ', goods_list[key][1])
        print('----------------------')
        continue
print('', 'n', ' ', goods_list['n'])


#用户选择需要做的操作：查看余额、充值、购买商品
user_login_status = 1
while user_login_status == 1:#判断用户的登录状态
    user_action = int(input('请选择您要执行的操作：\n1.查看账户余额(请输入：1) \n2.给账户充值(请输入：2) \n3.购买商品(请输入：3) \n4.退出系统(请输入：4) \n'))
    if user_action == 1:#查看账户余额
        print('你的余额是：' + str(user_account_balance))
        print()
    elif user_action == 2:#给账户充值
        while True:
            money_recharge = input('请输入你要充值的金额：')
            if money_recharge.isdigit():
                user_account_balance += int(money_recharge)
                print('充值成功，您的账户余额为：' + str(user_account_balance))
                print()
                break
            else:
                print('输入金额错误，请重新输入\n')
                continue
    elif user_action == 3:#购买商品
        user_shopping_list = {}  # 用户购物清单
        while True:
            goods_num = input('请选择你要购买的商品序号：')
            if goods_num != 'n':
                goods_num = int(goods_num)
                if goods_num in goods_list:
                    user_shopping_goods_num = 1
                    user_shopping_goods_name = goods_list[goods_num][0]
                    user_shopping_goods_price = goods_list[goods_num][1]
                    user_shopping_list[user_shopping_goods_name] = [user_shopping_goods_num,user_shopping_goods_price]
                    user_shopping_goods_num += 1
            elif goods_num == 'n':
                print('结算')
                print(user_shopping_list)
                break
            else:
                print('输入有误，请重新输入')
            continue


