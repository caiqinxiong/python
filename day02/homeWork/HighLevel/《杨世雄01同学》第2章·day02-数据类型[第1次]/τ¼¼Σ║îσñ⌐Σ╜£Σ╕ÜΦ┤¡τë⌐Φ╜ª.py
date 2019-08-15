product_list = {
    1:('手机',5800),
    2:('电脑',9800),
    3:('鼠标',1000),
    4:('键盘',1060),
    5:('硬盘',3100),
    6:('音箱',1200),
    'n':('购物车','')
}
user_info ={
    'banance':0,
    'shopping list':{}
}
while True:
    balance = input('please input your balance:').strip()
    if balance.isdigit():
        user_info['banance'] = int(balance)
        break
    elif balance.upper() == 'Q':
        break
    else:
        print('the input information, please re-input!')
key_list = []
choice_list = []
while True:
    print('产品列表'.center(30,'-'))
    print('         '+'编号' + '  '+'产品'+'  '+'单价')
    for key in product_list:
        print('         ',key,' ',product_list[key][0],' ',product_list[key][1])
        key_list.append(key)
    for choice in user_info['shopping list']:
        choice_list.append(choice)
    user_choice = input('请输入你要买的商品编号').strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice in key_list:
            if user_choice in choice_list:
                user_info['shopping list'][user_choice][1] += 1
            else:
                user_info['shopping list'][user_choice] = [product_list[user_choice],1]
            print('你已经添加了%s到购物车, 单价是%s元, 现在购物车里有%s数量是%s ' % (product_list[user_choice][0],product_list[user_choice][1],product_list[user_choice][0],user_info['shopping list'][user_choice][1]))
            continue
        else:
            print('没有这个编号的商品，请重新选择!')
    elif user_choice.upper() == 'Q':
        print('谢谢光临，欢迎下次再来，再见！')
        break
    elif user_choice.lower() == 'n':
        money = 0
        for key in user_info['shopping list']:
            money += user_info['shopping list'][key][0][1] * user_info['shopping list'][key][1]
        while user_info['banance'] < money:
            print("你没有足够的钱去买所有购物的的商品, 你只有 %s元, 购物车的商品总额是%s元，请删除一些" % (user_info['banance'],money))
            print('         '+'编号' + '  '+'产品'+'   '+'单价'+'  ' +'数量')
            key_list2 = []
            for key in user_info['shopping list']:
                print('         ',key,' ',user_info['shopping list'][key][0][0],' ',user_info['shopping list'][key][0][1],' ',user_info['shopping list'][key][1])
                key_list2.append(key)
            user_choice = input('请选择你要删除的项目').strip()
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice in key_list2:
                    money -= user_info['shopping list'][user_choice][0][1]
                    print('你已经删除了1个 %s' %product_list[user_choice][0])
                    user_info['shopping list'][user_choice][1] -=1
                    if user_info['shopping list'][user_choice][1] == 0:
                        print('%s已经在购物车中清空啦'%user_info['shopping list'][user_choice][0][0])
                        del user_info['shopping list'][user_choice]
                else:
                    print('购物车中没有这个产品，请重新选择!')
            elif user_choice.upper() == 'Q':
                print('谢谢光临，欢迎下次再来，再见！')
                break
            else:
                print('输入有误，请重新输入')

        else:
            user_info['banance'] -=money
            print('已购商品'.center(40,'-'))
            print('         '+'编号' + '  ' + '产品' + '   ' + '单价' + '  '+'数量')
            for key in user_info['shopping list']:
                print('         ',key,' ',user_info['shopping list'][key][0][0],' ',user_info['shopping list'][key][0][1],' ',user_info['shopping list'][key][1])
            print('你买了%s元的商品, 你还剩%s元, 谢谢光临，欢迎下次再来，再见!'%(money,user_info['banance']))
            break
    else:
        print('输入信息有无，请重新输入!')

