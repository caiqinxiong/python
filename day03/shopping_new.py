# -*- coding:utf-8 -*-
# Author:caiqinxiong
import os
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#os.popen('sed -i ""  "s#Pen.*#Pen 10#g" goods_list.txt')

'''
product_list = [
    ('Iphone',5800),
    ('Mac Pro', 12000),
    ('Bike',800),
    ('Watch',15000),
    ('Coffer',46),
    ('Book',70)
]
'''
user = input('are you user or business:')
if user == 'user':
    product_list = []
    with open('goods_list.txt', 'r') as p:
        for line in p.readlines():
            line = line.strip().split(' ')
            #print(line)
            product_list.append(line)
        #print(product_list)
    p.close()

    shopping_list = []
    if os.path.exists('shooping_list.txt'):
        salary = os.popen("tail -n 1 shooping_list.txt | awk -F : '{print $NF}'").read()
        #salary = os.system('tail -n 1 shooping_list.txt')
        print("Your current balance:",salary)
    else:
        salary = input("Please input your salary:")
        if not salary.isdigit():
            print('输入有误！')
            exit()

    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("Please choice wath do you want to buy:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                p_item[1] = int(p_item[1])
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added [%s] into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item,salary))
                else:
                    print("\033[41;1m you have no more money!! \033[0m")
                    exit()
            else:
                print("product code [%s] is no exist!!" % user_choice)
        elif user_choice == 'q':
            print("##########shopping list###########")
            with open('shooping_list.txt', 'a+') as s:
                s.write( '\n' +nowTime + '\n')
                for p in shopping_list:
                    print(p)
                    s.write(str(p) + '\n')
                print("Your current balance:",salary)
                s.write("Your current balance:" + str(salary) + '\n')
            s.close()
            exit()
        else:
            print("invalid option")
elif user == 'business':
    print('''
    1 添加商品
    2 修改商品价格
    ''')
    choice = input()
    if choice == '1':
        product = input('请输入要添加的商品名称：')
        price = input('请输入该商品价格：')
        with open('goods_list.txt', 'a+') as g:
            g.write(product + ' ')
            g.write(price + '\n')
        g.close()
        print("已经添加：%s\t%s" % (product,price))
    elif choice == '2':
        product_list = []
        with open('goods_list.txt', 'r') as p:
            for line in p.readlines():
                line = line.strip().split(' ')
                print(line)
                product_list.append(line)
            print(product_list)
        p.close()
        product = input('请输入要修改的商品名称：')
        awk = os.popen("awk '{print $1}' goods_list.txt").read()
        __product_list = list(awk.strip().split('\n'))
        if not product in __product_list:
            print("输入的商品不存在！")
        else:
            price = input('价格修改为：')
            os.popen('sed -i ""  "s#%s.*#%s %s#g" goods_list.txt'%(product,product,price))
            print("已经将%s的价格修改为：%s" % (product,price))
    else:
        print('输入有误！')

else:
    print('have not this guy!')