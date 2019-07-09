# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/7 下午4:04
ball_list = []
while True:
    choice = input('请选择6个红球（红球的选择范围是1-32)')
    if choice.isdigit():
        choice= int(choice.strip())
        if choice > 0 and choice < 33:
            if choice in ball_list:
                print('选择的数字重复了！')
                continue
            ball_list.append(choice)
            print('选择的第\033[35;5m%s\033[5m个红球的号码为：\033[31;1m%s\033[0m' % (len(ball_list),choice))
        else:
            print('红球的选择超出范围！！')
        if len(ball_list) == 6:
            while True:
                choice = input('请选择2个蓝球（篮球的选择范围是1-16)')
                if choice.isdigit():
                    choice = int(choice.strip())
                    if choice > 0 and choice < 17:
                        if choice in ball_list:
                            print('选择的数字重复了！')
                            continue
                        ball_list.append(choice)
                        print('选择的第\033[36;5m%s\033[5m个蓝球的号码为：\033[34;1m%s\033[0m' % (len(ball_list)-6, choice))
                    else:
                        print('红球的选择超出范围！！')
                    if len(ball_list) == 8:
                        print('分割线'.center(50,'-'))
                        print('您选择的双色球的号码为：')
                        # print('\033[0;44;37m%s\033[0m' % ball_list)
                        for i in ball_list:
                            if ball_list.index(i) > 5:
                                print('\033[0;44;37m%s\033[0m' % i, end=' ')
                            else:
                                print('\033[41;1m%s\033[0m' % i, end=' ')
                        exit(-1)
                else:
                    print('请输入有效数字！')
    else:
        print('请输入有效数字！')