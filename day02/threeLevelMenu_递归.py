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
#print(menu)
# 递归函数
def threeLM(dic):
    while True:
        for k in dic:
            print(k)
        key = input('input>>').strip()
        if key == 'b' or key == 'q':
            print('bbb')
            return key

        elif key in dic.keys() and dic[key]:
            print(dic[key])
            ret = threeLM(dic[key]) #再次调用函数，相当于循环，调用了几次，就需要几个return才能结束。
            if ret == 'q':
                print('qqqq')
                return 'q'

if __name__ == '__main__':
    #threeLM(menu)
    # 只能回退一层
    print('欢迎使用三级菜单小程序！')
    while True:
        for name in menu:
            print(name)
        choise = input('请选择：').strip()
        if choise in menu.keys() and menu[choise]:
            super_dict = menu
            menu = menu[choise]
        elif 'B' == choise.upper():
            menu = super_dict
        elif 'Q' == choise.upper():
            print('谢谢使用！')
            exit(-1)
        elif choise in menu.keys() and menu[choise] == {}:
            print('人家是有底线的（已经是最底层）！！')
        else:
            print('输入有误！')









