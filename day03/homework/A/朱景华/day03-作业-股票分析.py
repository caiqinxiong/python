#_author:"ZhuJH"
#date:2019/7/26

f_dict = {}         # 查找 最新<5 之类的数据，这里定义的是一个字典 ；
f_list = []         # 查找类似 科技 能源 食品的数据,这里定义了一个列表 ；
with open(r'stock_data.txt', mode='r', encoding='utf-8') as f:
    f_title_list = f.readline().split(',')      # 获取第一行的菜单

    for line in f:
        f_list.append(line)        # 为了菜单的格式 先扩增了列表
        #print(line)
        line = line.split(',')
        f_dict.setdefault(line[2], {})  # 以股票名字为key，具体的数据为value，创建二维菜单
        for k, item in enumerate(line):
            f_dict[line[2]].setdefault(f_title_list[k], item)


while True:
    count = 0
    choice = input("股票查询接口>>>:").strip()  # 去空格 # 最新价<5
    if '<' in choice:
        choice_of_first, choice_of_last = choice.split('<')
        for k, v in f_dict.items():
            num = v[choice_of_first].split('%')[0]  # 去掉数据中的%，转成float比较
            num = float(num)
            choice_of_last = float(choice_of_last)
            if num < choice_of_last:
                print(k, "其{0}为：{1}".format(choice_of_first, num))
                count += 1
        print('一共有%d条数据' % count)

    elif '>' in choice:
        choice_of_first, choice_of_last = choice.split('>')     ## 换手率>25
        for k, v in f_dict.items():
            num = v[choice_of_first].split('%')[0]     # 拿到相应的数据，去掉% 转成float
            num = float(num)
            choice_of_last = float(choice_of_last)
            if num > choice_of_last:
                count += 1
                print(k, "其{0}为：{1}".format(choice_of_first, num))
        print('一共有%d条数据'% count)
    else:
        for item in f_title_list: print(item, end=' ')
        for k in f_dict.keys():
            if choice in k:
                count += 1
                index_num = int(f_dict[k]['序号']) - 1
                print(f_list[index_num])
        print('找到%d条' % count)