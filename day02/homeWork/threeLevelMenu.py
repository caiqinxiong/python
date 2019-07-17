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
def threeLM(dic):
    while True:
        for k in dic:
            print(k)
        key = input('input>>').strip()
        if key == 'b' or key == 'q':
            print('aaa')
            return key

        elif key in dic.keys() and dic[key]:
            ret = threeLM(dic[key])
            if ret == 'q':
                print('qqqq')
                return 'q'

threeLM(menu)
