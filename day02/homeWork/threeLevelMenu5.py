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
choise_list = []
def threeLevelMenu(menu):
    while True:
        # 打印字典
        print('~'*20)
        for name in menu:
            print(name)

        choise = input('请选择：').strip()
        if choise in menu.keys() and menu[choise]:
            if not choise in choise_list:
                choise_list.append(choise)
            #print(menu[choise])
            #print(choise_list)
            threeLevelMenu(menu[choise]) # 再次调用函数，相当于循环，调用了几次，就需要几个return才能结束。
        elif 'B' == choise.strip().upper():
            #print(choise_list)
            if len(choise_list) == 0:
                print('~' * 20)
                print('\033[31;1m已经是最顶层啦！\033[0m')
            else:
                print('~' * 20)
                print('\033[34;1m返回上层啦！\033[0m')
                choise_list.pop()
                return choise
        elif 'Q' == choise.strip().upper():
            print('\033[36;5m谢谢使用！\033[5m')
            exit(-1)
        else:
            try: # 处理key值异常 # 可以用字典的get方法
                if menu[choise] == {}:
                    print('~' * 20)
                    print('\033[31;1m已经是最底层啦！返回上层按b,退出按q！\033[0m')
            except:
                print('输入有误，请重新输入！')


if __name__ == '__main__':
    print('~' * 20)
    print('\033[36;5m欢迎使用三级菜单小程序！\033[5m')
    threeLevelMenu(menu)
