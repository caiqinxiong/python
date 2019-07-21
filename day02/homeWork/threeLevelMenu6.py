# -*- coding:utf-8 -*-
# 王刘俊
# 2019/7/17 下午11:37
menu_dic = {
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

current_level = menu_dic
record = []

'''
1.遍历当前菜单current_level（初始值为menu_dic）
2.每进入一级前,先将当前级保存至record，current_level重新赋值为所选菜单
3.客户选择back时，将上级菜单用pop()从record中移除，并将返回值重新赋值给current_level
'''
while True:
    # 遍历当前菜单
    for i in current_level:
        print(i)
    choice = input('>>请选择(b返回q退出):')
    choice = choice.strip()
    if choice.upper() == 'Q':
        break
    elif choice.upper() == 'B':
        if not record:
            print('已经是顶层')
            continue
        current_level = record.pop()  # 3.返回步骤1记录的最后一项菜单
    elif choice in current_level:
        if not len(current_level[choice]):
            print('已是最底层')
            continue
        record.append(current_level)  # 1.进入下一级菜单前，将当前菜单记录下来
        current_level = current_level[choice]  # 2.进入下一级菜单
        #print(current_level)
    else:
        print('指令无效')