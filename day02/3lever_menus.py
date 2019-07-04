# -*- coding:utf-8 -*-
# Author:caiqinxiong

date = {
    '北京' : {
        '昌平':{
            '沙河':['oldboy','caiqinxiong'],
            '天通苑':['链家地产','我爱我家']
        },
        '朝阳':{
            '望京':['奔驰','陌陌'],
            '国贸':['CCIC','HP'],
            '东直门':['Advert','飞信']
        },
        '海淀':{}
    },
    '山东':{
        '德州':{},
        '青岛':{},
        '济南':{}
    },
    '广东':{
        '东莞':{},
        '广州':{},
        '佛山':{ }
    }
}

while True:
    for i in date:
        print(i)
    choice = input('请选择进入1>>:')
    if choice in date:
        while True:
            for j in date[choice]:
                print('\t',j)
            choice2 = input('请选择进入2>>:')
            if choice2 in date[choice]:
                while True:
                    for k in date[choice][choice2]:
                        print('\t\t',k)
                    choice3 = input('请选择进入3>>:')
                    if choice3 in date[choice][choice2]:
                        for h in date[choice][choice2][choice3]:
                            print('\t\t\t',h)
                        choice4 = input('最后一层，请按b返回,q退出！')
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit()
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit()
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit()






