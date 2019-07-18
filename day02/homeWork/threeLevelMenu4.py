# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/17 下午11:37
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def printDict(menu):
    for i in menu:
        print(i)

def lverlOne():
    #print(11111111)
    while True:
        choise = input("请选择：").strip()
        if choise in menu:
            printDict(menu[choise])
            lverlTwo(choise)
            break
        elif 'B' == choise.upper():
            print('已经是最上层！')
            printDict(menu)
        elif 'Q' == choise.upper():
            exit(-1)
        else:
            print("输入错误，请重新输入!")

def lverlTwo(lverlOne_chise):
    #print(22222222)
    while True:
        choise = input("请选择：").strip()
        if choise in menu[lverlOne_chise]:
            printDict(menu[lverlOne_chise][choise])
            lverlThree(lverlOne_chise,choise)
            break
        elif 'B' == choise.upper():
            printDict(menu)
            lverlOne()
            break
        elif 'Q' == choise.upper():
            exit(-1)
        else:
            print("输入错误，请重新输入!")

def lverlThree(lverlOne_chise,lverlTwo_chise):
    #print(3333333)
    while True:
        choise = input("请选择：").strip()
        if choise in menu[lverlOne_chise][lverlTwo_chise]:
            printDict(menu[lverlOne_chise][lverlTwo_chise][choise])
            lverlFour(lverlOne_chise,lverlTwo_chise,choise)
        elif 'B' == choise.upper():
            printDict(menu[lverlOne_chise])
            lverlTwo(lverlOne_chise)
            break
        elif 'Q' == choise.upper():
            exit(-1)
        else:
            print("输入错误，请重新输入!")


def lverlFour(lverlOne_chise,lverlTwo_chise,lverThree_choise):
    #print(4444444)
    while True:
        choise = input("请选择：").strip()
        if choise in menu[lverlOne_chise][lverlTwo_chise][lverThree_choise]:
            print('已经是最后一层啦！返回上层按b,退出按q！')
        elif 'B' == choise.upper():
            printDict(menu[lverlOne_chise][lverlTwo_chise])
            lverlThree(lverlOne_chise,lverlTwo_chise)
            break
        elif 'Q' == choise.upper():
            exit(-1)
        else:
            print("输入错误，请重新输入!")



if __name__ == '__main__':
    print('欢迎使用三级菜单小程序！')
    printDict(menu)
    lverlOne()