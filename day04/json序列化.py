# -*- coding:utf-8 -*-
# Author:caiqinxiong
import json #主要用于不同语言之间的转换，list，dict，str等，函数不行。
import pickle #用法和json一样，支持所以类型转换,二进制形式,只能在python里用
def sayHi(name):
    print('Hi',name)

info = {
    'name':'lixiaoxin',
    'age':30,
    'func':sayHi
}
#f = open('info.txt','w')
f = open('info.txt','wb')
#f.write(str(info)) #将字典转字符串，序列化。
#print(json.dumps(info))#序列化，dumps不是dump
#f.write(json.dumps(info))
#f.write(pickle.dumps(info))
pickle.dump(info,f)#等价于 f.write(pickle.dumps(info))，不要写write了
f.close()
print('################################')
#f = open('info.txt','r')
f = open('info.txt','rb')
#data = eval(f.read())#反序列化
#data = json.loads(f.read())#反序列化，loads不是load
#data = pickle.loads(f.read())#反序列化，loads不是load
data = pickle.load(f)#等价于 data = pickle.loads(f.read())，不用写read了
f.close()
print(data)
print(data['age'])
print('################################')
print(data['func'])
print(data['func']('lixiaoxin'))