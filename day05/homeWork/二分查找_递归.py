# -*- coding: utf-8 -*-
# 2019/8/5 11:07
#参考女神博客链接：https://www.cnblogs.com/Eva-J/articles/7197403.html

def binary_search(num,list_info,start=None,end=None):
    '''
    二分查找
    :param num:要查找的数
    :param list_info:列表信息
    :param start: 搜索开始index值
    :param end:搜索结束index值
    :return:搜索到时返回该数在列表中的index值，否则返回None
    '''
    start = start if start else 0 # 三元运算，如果搜索开始位置不为零，则将新值赋给start。
    end = end if end is not None else len(list_info) - 1 # 三元运算，如果搜索结束位置不为空，则将列表最后的索引值给end，len(list_info) - 1为list最后的索引值，因为index从0开始
    mid = (end - start)//2 + start # 获取中间位置的index值，这里用了地板除，确保能获取到整数。
    if start > end: # 搜索开始index值大于结束index值，说明已将list搜索完成。
        return None
    elif list_info[mid] > num : # 如果中间索引的数大于要搜索的数，则要查找的数在二分的前面，将mid-1赋值给end。再继续递归查找。
        return binary_search(num,list_info,start,mid-1) # 递归调用
    elif list_info[mid] < num: # 如果中间索引的数小于要搜索的数，则要查找的数在二分的后面，将mid-1赋值给start。再继续递归查找。
        return binary_search(num,list_info,mid+1,end) # 递归调用
    elif list_info[mid] == num: # 如果中间索引的数刚好等于要搜索的数，则返回搜索结果。
        return mid

while True:
    list_info = [2,3,5,7,9,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88,93,100]
    print('列表信息如下：\n',list_info)
    choise = input('请输入要查找的数：').strip()
    if choise.isdigit():
        choise = int(choise)
        ret = binary_search(choise,list_info)
        if ret != None:
            print('\033[31;1m%s\033[0m在搜索列表里的第\033[31;1m%s\033[0m个位置！' % (choise,list_info.index(choise)+1))
        else:
            print('\033[31;1m%s\033[0m不在搜索列表里' % choise)
        break
    else:
        print('输入有误，请重新输入！')