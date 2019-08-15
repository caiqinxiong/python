# 作业题目: 购物车
# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 商品名称 + 商品价格，如：
#         1 电脑 1999
#         2 鼠标 10
#         …
#         n 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，
#    若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。(这一步还在想)
# 6. 用户输入Q或者q退出程序。
# 7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。

#  解题思路：
# 首先输入工资的金额
    # 打印商品清单
    # 输入商品序列号
    # 判断商品的金额 >工资的金额
        # 如果大于
            # 显示余额不足
        # 如果小于等于
            # 购买商品加入购物车
            # 工资减去商品的金额
    # 判断用户输入"N"  或 "n"
#        打印购物车清单
#        购物车的商品可删除  （暂时还没实现）
#        工资余额充足继续购买
    # 判断用户输入"Q"  或 "q"
#         打印购物清单
#         退出程序

article = [
    {'name':'电脑','price':1900},
    {'name':'电动车','price':2900},
    {'name':'电风扇','price':900},
    {'name':'电饭煲','price':2900},
]

shopping_cart = []

wage = input('请输入您的工资： ').strip()

if wage.isdigit():    #检查输入是否为字母数字
    wage = int(wage)
    while True:
        for index,item in enumerate(article):  #取商品清单
            print('%s  %s %s' %(index,item['name'],item['price']))
        selectd = input('>>>').strip()         #选择商品的序号
        if selectd.isdigit():
            selectd = int(selectd)
            if selectd >= 0 and selectd < len(article):  #判断商品的序号是否超过当前的取值
                selectd_item = article[selectd]
                if selectd_item['price'] <= wage:        #判断商品的金额是否大于工资额度
                    shopping_cart.append(selectd_item)   #商品加入购物车
                    wage -= selectd_item['price']        #工资减去商品的金额
                    print('已添加[%s]到您的购物车，余额还剩[%s]' %(selectd_item['name'],wage))
                else:
                    print('余额不足')
        elif selectd == 'N' or selectd == 'n':   #打印购买清单
            print('已购买商品'.center(30,'-'))
            for index,item in enumerate(shopping_cart):
                print('%s  %s  %s' % (index, item['name'], item['price']))
            print('余额还剩下 %s ' % wage)
        elif selectd == 'Q' or selectd == 'q':   #打印购买清单并退出
            print('已购买商品'.center(30,'-'))
            for index,item in enumerate(shopping_cart):
                print('%s  %s  %s' % (index, item['name'], item['price']))
            print('余额还剩下 %s ' % wage)
            exit()
        elif selectd.isalpha():   #检查输入是否为字母
            print('您输入有错，请再次输入商品序列号')




