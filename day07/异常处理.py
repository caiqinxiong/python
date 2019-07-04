# -*- coding:utf-8 -*-
# Author:caiqinxiong

date = {'name':"caiqinxiong",'age':29}
names = ['cai','li']

# print(date['name'])
try:
    #print(names[3])
    #print(date['hobby'])
    open('aa.txt')
    print('hahaha')
except KeyError as e: # 获取key值异常
    print('has not key:',e)
except IndexError as e:
    print('has no index:',e)
except Exception as e: # 能抓住大部分的异常,如果无法判断错误类型的话，放在最后用。
    print('出错了，但是只能自己根据错误信息判断是什么错误了',e)
else:
    print('一切正常')
finally:
    print("不管你有没有错，都执行！！！")
