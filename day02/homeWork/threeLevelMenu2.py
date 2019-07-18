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
# 只能输入两层，然后回退
print('欢迎使用三级菜单小程序！')
tmp_dic = menu
choise_list = []
n = 1
while True:
    for name in tmp_dic:
        print(name)
    choise = input('请选择：').strip()
    if choise in tmp_dic.keys() and tmp_dic[choise]:
        if not choise in choise_list:
            choise_list.append(choise)
        #print(choise_list)
        super_dict = tmp_dic
        tmp_dic = tmp_dic[choise]
    elif 'B' == choise.upper():
        tmp_dic = super_dict
        choise_list.pop()
        if n == 2:
            tmp_dic = menu
            n -= 2
        n += 1
        #print(n)
    elif 'Q' == choise.upper():
        print('谢谢使用！')
        exit(-1)
    elif choise in tmp_dic.keys() and tmp_dic[choise] == {}:
        print('已经是最底层！！')
    else:
        print('输入有误！')








