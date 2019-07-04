# -*- coding:utf-8 -*-
# Author:caiqinxiong

product_list = [
    ('Iphone',5800),
    ('Mac Pro', 12000),
    ('Bike',800),
    ('Watch',15000),
    ('Coffer',46),
    ('Book',70)
]
shopping_list = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("Please choice wath do you want to buy:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
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
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("invalid option")