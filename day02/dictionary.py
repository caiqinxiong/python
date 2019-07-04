# -*- coding:utf-8 -*-
# Author:caiqinxiong
__dict = {
    '01':'caiqinxiong',
    '02':'lixiaoxin',
    '03':'hahaha'
}
#字典打印是无序都，有key，所以不需要下标
print(__dict)
#修改
__dict['03'] = 'mama'
print(__dict)
#删除
#del __dict
#del __dict['03']
print(__dict.pop('02'))
print(__dict)
#增加
__dict['04'] = 'aaaaaa'
print(__dict)
#查找
print(__dict['04'])
#print(__dict['05'])
print(__dict.get('04'))
print(__dict.get('05'))

print('03' in __dict) #print(__dict.has_key('03')) python3没有这个方法了
print('caiqinxiong' in __dict) #只找key

#字典多级嵌套，三级菜单

info = { 'stu01' : 'caiqinxiong',
         'stu02' : 'lixiaoxin',
         'stu03' : 'nobody'
         }
print(info)
aa = {'stu01' : 'CAI',
      'aa' : 'AA',
      'bb' : 'BB'
      }
print(aa)
#将两个字典合并，更新
info.update(aa)
print(info)
#把字典转成list
print(info.items())
#字典初始化，三个key指向同一个内存地址
bb = dict.fromkeys(['a','b','c'],[111,{'name':'caiqinxiong'},222])
print(bb)
bb['b'][1]='lixiaoxin'#修改其中的一个值，三个全都变了,类似浅复制
print(bb)
#尽量用这种方式
for i in bb:
    #print(i)
    print(i,bb[i])
print("####################")
#字典转成list了，数据量大时不适合用
for k,v in bb.items():
    print(k,v)













