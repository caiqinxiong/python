# -*- coding:utf-8 -*-
# Author:caiqinxiong

#name = 'my\tname is caiqinxiong'
name = 'my\tname is {name} and I am {year} old'
#首字母大写
print(name.capitalize())
print(name.count('a'))
#字符串居中，50个字符，不够以"+"补齐
print(name.center(50,'+'))
#判断是否以该字符结尾
print(name.endswith('caiqinxiong'))
print(name.expandtabs(tabsize=30))
print(name.find('cai'))
print(name[name.find('cai'):])
print(name.format(name='caiqinxiong',year='28'))
print(name.format_map({'name':'cai','year':18}))
#只由大小写字母或数字组成
print(name.isalnum())
print('abc123:','abc123'.isalnum())
print('abc:','abc'.isalnum())
print('123','123'.isalnum())
print('abc123#$:','abc123#$'.isalnum())
print('abc123\t:','abc123\t'.isalnum())
print('abc123\t:','abc123\t'.isalnum())
#纯英文字符,可以是大小写
print('abcA:','abcA'.isalpha())
#整数
print('123.33:','123.33'.isdigit())
#判断是否是合法标示符
print('123:','123'.isidentifier())
print('_123:','_123'.isidentifier())
#是不是全小写
print('aaa:','aaa'.islower())
print('AAA:','AAA'.lower())
print('aaA:','aaA'.isupper())
print('aaA:','aaA'.upper())

#是不是空格
print('\t'.isspace())
print('  '.isspace())
#判断是不是title，每个首字母大小
print('My name is '.istitle())
print('My Name Is '.istitle())
print('+'.join(['1','2','3']))
print(','.join(['cai','qin','xiong']))
#保证左边，不够补字符
print(name.ljust(50,'*'))
#保证右 边，不够补字符
print(name.rjust(50,'*'))
#去除左边的空格或回车
print('-----------')
print('\ncaiqinxiong\n'.lstrip())
print('-----------')
print('\ncaiqinxiong\n'.rstrip())
print('-----------')
print('\ncaiqinxiong\n'.strip())
print('-----------')

#随机加密
p = str.maketrans('abcdef','123456')#前面字母和后面数字一一对应
print('caiqinxiong'.translate(p))
p = str.maketrans('abcdef_xiong','123456_@#$%&')#前面字母和后面数字一一对应
print('caiqinxiong'.translate(p))
#找到替换，前2个
print('caiqinxiong'.replace('i','I',2))
#查找，返回索引值
print('caiqinxiong'.rfind('i'))
print('caiqinxiong'.find('i'))
#返回list
print('caiqinxiong'.split('qin'))
#按行切割
print('cai\nqin\nxiong'.splitlines())
#大小写互换
print('CAIqinxoing'.swapcase())
#把首字母都大写
print('cai qin xiong'.title())
#不够50个字符前面补0
print('caiqinxiong'.zfill(50))




