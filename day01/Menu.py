# -*- coding:utf-8 -*-
# Author:caiqinxiong

print('''
##################################
        欢迎登陆XX购物系统
##################################
1 生鲜水果
2 休闲零食
3 家用电器
4 油粮厨房
''')
def fruit():
    print('''
        水果有以下几种：
        1 苹果
        2 香蕉
        3 西瓜
        4 凤梨
    ''')
def meat():
    print('''
        肉类有以下几种：
        1 猪肉
        2 牛肉
        3 鸡肉
        4 羊肉
    ''')
def fresh():
    print('''
    生鲜有以下几种：
    1 水果
    2 肉类
    ''')
    while True:
        selection = int(input("请选择:"))
        if selection == 1:
            fruit()
            break
        elif selection == 2:
            meat()
            break
        else:
            print("请输入有效数字！")

while True:
    selection = int(input("请选择:"))
    if selection == 1:
        fresh()
        break
    elif selection == 2:
        break
    elif selection == 3:
        break
    elif selection == 4:
        break
    else:
        print("请输入有效数字！")