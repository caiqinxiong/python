#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File  :  递归函数_三级菜单.py
@Time  :  2019/08/05 16:05:30
@Author:  赵臻 
'''

menu = {
    '北京':{
        '海淀区':{
            '中关村':{
                '中关村科技园':{},
                '爱奇艺': {},
                'youku': {},
             },
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {},
             },
        },
        '昌平区':{
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑':{
                '太平家园':{},
                '中福大厦':{},
            },
        },
        '朝阳区': {},
    },
    '上海':{
        '闵行': {
            '人民广场': {
                '炸鸡店': {},
            },
        },
        '闸北': {
            '火车站': {
                '携程': {},
            }
        },
        '浦东': {},
    },
    '广州':{
        '白云区':{
            '白云湖':{},
            '西湖':{},
            },
        '珠海区':{
            '珠海区政府':{},
            '珠影.星光城':{},
        },
        '天河区':{},
    },
    '北上广不相信眼泪':{
        '北京.上海.广州':{},
    },
}

#递归函数定义
def menu_func(func):
    while True:
        for k in func:print(k) # 循环输出key
        key = input(">>>>").strip() # 交互式输入内容
        if key.upper() == 'B':return # 判断输入b,返回上一层
        elif key.upper() == 'Q':exit() # 判断输入q,退出程序
        elif key in func:menu_func(func[key])  # 如果输入的kay存在于menu中,则递归
        else:print("sorry,输入错误,请重新输入")  # 以上均不匹配,提示输入错误
        menu_func(func[key])
menu_func(menu)