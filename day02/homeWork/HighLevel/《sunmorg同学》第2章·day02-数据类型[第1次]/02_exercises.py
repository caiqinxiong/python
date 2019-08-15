# '''
#     1、有变量name = "aleX leNb" 完成如下操作：
# '''
# name = 'aleX leNb'
# #去除两端空格
# print(name.strip())
# #移除变量左边'al'
# print(name.lstrip('al'))
# #移除变量右边'Nb'
# print(name.rstrip('Nb'))
# #移除变量开头'a'与结尾'b'
# print(name.strip('ab'))
# #判断变量是否以'al'开头
# print(name.startswith('al'))
# #判断变量是否以'Nb'结尾
# print(name.startswith('Nb'))
# #将变量中所有的'l'替换为'p'
# print(name.replace('l', 'p'))
# #将变量中的第一个'l'替换为'p'
# print(name.replace('l', 'p', 1))
# #将变量根据所有'l'分割
# print(name.split('l'))
# #将变量根据第一个'l'分割
# print(name.split('l', 1))
# #将变量对应的值变大写
# print(name.upper())
# #将变量对应的值变小写
# print(name.lower())
# #将变量对应的首字母变大写
# print(name.capitalize())
# #判断变量中'l'出现的次数
# print(name.count('l'))
# #判断变量中前4位'l'出现的次数
# print(name.count('l',0,4))
# #从name变量对应的值中找到"N"对应的索引(如果找不到则报错)
# print(name.index('N'))
# #从name变量对应的值中找到"N"对应的索引(如果找不到则返回‐1)
# print(name.find('N'))
# #从name变量对应的值中找到"X le"对应的索引,并输出结果
# print(name.find('X le'))
# #输出变量第二个字符
# print(name[1])
# #输出变量前三个字符
# print(name[:3])
# #输出变量后两个字符
# print(name[-2:])
# #输出变量'e'的索引
# for i in range(len(name)):
#     if name[i] == 'e':print(i)


# '''
#     2、有字符串s = "123a4b5c" 完成如下操作：
# '''
# s = "123a4b5c"
# #通过对s切片形成新的字符串s1,s1 = "123"
# s1 = s[:3]
# #通过对s切片形成新的字符串s2,s2 = "a4b"
# s2 = s[3:-2]
# print(s2)
# #通过对s切片形成新的字符串s3,s3 = "1345"
# s3 = ''
# for i in s:
#     if i.isdigit():
#         s3 += i
# print(s3)
# #通过对s切片形成字符串s4,s4 = "2ab"
# s4 = s[1:-2:2]
# print(s4)
# #通过对s切片形成字符串s5,s5 = "c"
# s5 = s[-2:-1]
# print(s5)
# #通过对s切片形成字符串s6,s6 = "ba2"
# s6 = s[-3:0:-2]
# print(s6)

# '''
#     3、使用while或for循环分别打印字符串s="asdfer"中每个元素。
# '''
# s = "asdfer"
# for i in s:
#     print(i)

# '''
#     4、使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
# '''
# s = "asdfer"
# for i in s:
#     print(s)

# '''
#     5、使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb，例如：asb, bsb，csb,...gsb。
# '''
# for i in s:
#     print("%ssb"%(i))

# '''
#     6、使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# '''
# s = '321'
# for i in s:
#     print("倒计时%s秒"%(i))
#     if i == '1':print('出发！')

# '''
#     7、实现一个整数加法计算器(两个数相加)：
#         如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# '''


# '''
#     8、升级题：实现一个整数加法计算器（多个数相加）：
#         如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
# '''
# content = input("请输入内容:").replace(' ','')
# count = 0
# splitContent = content.split('+')
# for i in splitContent:
#     if i == '':
#         i = 0
#     else:
#         i = int(i)
#     count += i
# print(count)

# '''
#     9、计算用户输入的内容中有几个整数（以个位数为单位）。
#         如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
# '''
# content = input("请输入内容：")
# num_count = 0
# for i in content:
#     if i.isdigit():
#         num_count += 1
# print(num_count)

# '''
#     10、写代码，完成下列需求：用户可持续输入（用while循环），用户使用的情况：
#         输入A，则显示走大路回家，然后在让用户进一步选择：是选择公交车，还是步行？
#             选择公交车，显示10分钟到家，并退出整个程序。
#             选择步行，显示20分钟到家，并退出整个程序。
#         输入B，则显示走小路回家，并退出整个程序。
#         输入C，则显示绕道回家，然后在让用户进一步选择：是选择游戏厅玩会，还是网吧？
#             选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
#             选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
# '''
# while True:
#     choose_info = input("请选择回家方式，可选值A、B、C：").upper()
#     if choose_info == 'A':
#         print('走大路回家!')
#         choose_type = input('选择公交车，还是步行？').strip()
#         if choose_type == '公交车':
#             print('10分钟到家!')
#             break
#         elif choose_type == '步行':
#             print('20分钟到家!')
#             break
#         else:
#             print('错误的选项！')
#     elif choose_info == 'B':
#         print('走小路回家!')
#         break
#     elif choose_info == 'C':
#         print('绕道回家!')
#         choose_gamer = input('选择游戏厅玩会，还是网吧？').strip()
#         if choose_gamer == '游戏厅':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#             continue
#         elif choose_gamer == '网吧':
#             print('两个小时到家，妈妈已做好了战斗准备。')
#             continue
#         else:
#             print('错误的选项！')
#     else:
#         print('错误的选项！')
# '''
#     11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# '''
# num = 0
# for i in range(100):
#     if i%2 == 0:
#         if i != 88:
#             num = num - i
#     else:
#         num = num + i
# print(num)

# '''
#     16、制作趣味模板程序需求：等待户输名字、地点、爱好，根据户的名字和爱好进任意现实
#         如：敬爱可亲的xxx，最喜欢在xxx地xxx
# '''
# username = input('请输入用户名：')
# address = input('请输入地点：')
# hobby = input('请输入爱好：')
# print('尊敬可爱的%s,最喜欢在%s地%s'%(username,address,hobby))

# '''
#     17、等待户输内容，检测户输内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输”，并允许户重新输并打印。敏感字符：“粉嫩”、“铁锤”
# '''
# while True:
#     content = input('请输入内容：')
#     if '粉嫩' in content or '铁锤' in content:
#         print('存在敏感字符请重新输')
#     else:
#         print(content)
#         break

# '''
#     18、写代码，有如下列表，按照要求实现每一个功能
#         li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# '''
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# #1)计算列表的长度并输出
# print(len(li))
# #2)列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# print(li)
# #3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,'Tony')
# print(li)
# #4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = 'Kelly'
# print(li)
# #5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend([1,"a",3,4,"heart"])
# print(li)
# #6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend("qwert")
# print(li)
# #7)请删除列表中的元素"eric",并输出添加后的列表
# # li.remove('eric')
# print(li)
# #8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1))
# print(li)
# #9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)
# #10)请将列表所有得元素反转，并输出反转后的列表
# li.reverse ()
# print(li)
# #11)请计算出"alex"元素在列表li中出现的次数，并输出该次数
# print(li.count('alex'))

# '''
#     19、写代码，有如下列表，利用切片实现每一个功能
# '''
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# #1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# l1 = li[0:3]
# print(l1)
# #2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# l2 = li[3:6]
# print(l2)
# #3)通过对li列表的切片形成新的列表l3,l3 = [1,2,4,5]
# l3 = li
# del l3[1::2]
# print(l3)
# #4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# l4 = li
# l4 = l4[0:-2]
# del l4[0::2]
# print(l4)
# #5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
# l5 = li[-1:]
# print(l5)
# #6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# l6 = li[-3:0:-1]
# del l6[1::2]
# print(l6)
'''
    20、写代码，有如下列表，按照要求实现每一个功能。
'''
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# #1)将列表lis中的"tt"变成大写（用两种方式）。
# #方法一： 
# lis[3][2][1][0] = 'TT'
# #方法二： upper
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# #2)将列表中的数字3变成字符串"100"（用两种方式）。
# #方式一
# lis[1] = 100
# lis[3][2][1][1] = 100
# #方式二
# lis[1] += 97
# lis[3][2][1][1] += 97
# print(lis)
#3)将列表中的字符串"1"变成数字101（用两种方式）。
# #方式一
# lis[3][2][1][2] = 1
# #方式二
# lis[3][2][1][2] = int(lis[3][2][1][2])
# print(lis)

'''
    21、请用代码实现：
        li = ["alex", "eric", "rain"]利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
'''
# li = ["alex", "eric", "rain"]
# str = ''
# for index in range(len(li)):
#     if index < 2:
#         str = str + li[index] + '_'
#     else:
#         str = str + li[index]
# print(str)

'''
    22、利用for循环和range打印出下面列表的索引。
        li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for index in range(len(li)):
#     print(li[index])

# for i in li:
#     print(i)
'''
    23、利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中
'''
# num = []
# for index in range(101):
#     if index%2 == 0:
#         num.append(index)
# print(num)

'''
    24、利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
'''
# num = []
# for index in range(51):
#     if index%3 == 0:
#         num.append(index)
# print(num)

'''
    25、利用for循环和range从100~1，倒序打印。
'''
# for index in range(100,0,-1):
#     print(index)

'''
    26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
'''
# even_num = []
# for index in range(100,9,-2):
#     print(index)
#     even_num.append(index)
# print(even_num)
# for i in range(len(even_num)-1,-1,-1):
#     if even_num[i] % 4 != 0:
#         del even_num[i]
# print(even_num)

'''
    27、查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
'''
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# new_li = []
# for i in li:
#     i = i.strip()
#     if (i.startswith('a') or i.startswith('A')) and i.endswith('c'):
#         new_li.append(i)
# for i in new_li:print(i)

'''
    28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
    则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
'''
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# new_li = []
# while True:
#     content = input('输入评论内容：')
#     if len(content) > 0:
#         for i in li:
#             if i in content:
#                 content = content.replace(i,'*'*len(i))
#         new_li.append(content)
#     else:
#         print('请输入评论内容！')
#     print(new_li)
    
'''
    29、有如下变量（tu是个元祖），请实现要求的功能tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
        a. 讲述元祖的特性
        b. 请问tu变量中的第一个元素 "alex" 是否可被修改？
        c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
        d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
'''

'''
答案：
    a.元组tuple是不可改变的数据类型，不能修改元组中的元素，不能删除元素，不能添加元素。元组是受限制的列表。不能对元组进行排序。
    b.不可以被修改
    c.是列表类型，可以被修改，方法：tu[1][2]['k2'].append('Seven')
    d.是元组类型，不可以被修改
'''

'''
   30、字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
'''

# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# #a. 请循环输出所有的key
# for key in dic.keys():
#     print(key)
# #b. 请循环输出所有的value
# for v in dic.values():
#     print(v)
# #c. 请循环输出所有的key和value
# for k,v in dic.items():
#     print(k,v)
# #d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'alex'
# print(dic)
# #e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# #f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
# #g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)

'''
    31、如下
        
'''
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x‐art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#     },
#     "日韩":{
#         "tokyo‐hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
# # a,给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'。
# av_catalog['欧美']['www.youporn.com'].insert(1,'量很大')
# print(av_catalog)
# # b,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog['欧美']['x‐art.com'].remove('全部收费,屌丝请绕过')
# print(av_catalog)
# # c,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# # d,将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog['日韩']['tokyo‐hot'][1] = av_catalog['日韩']['tokyo‐hot'][1].upper()
# print(av_catalog)
# # e,给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog['大陆']['1048'] = ['一天就封了']
# print(av_catalog)
# # f,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# av_catalog['欧美'].pop('letmedothistoyou.com')
# print(av_catalog)
# # g,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog['大陆']['1024'][0] = '可以爬下来' + av_catalog['大陆']['1024'][0]
# print(av_catalog)
'''
    32、有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
'''
    
s = 'k:1|k1:2|k2:3|k3:4'
dic = {}
items = s.split('|')
for x in items:
    k, v = x.split(':')
    dic[k] = int(v)
print(dic) 

'''
    33、元素分类有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于66 的值保存至第二个key的值中。
    即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {'k1':[], 'k2':[]}
for i in li:
    if i > 66:
        dic['k1'].append(i)
    if i < 66:
        dic['k2'].append(i)
print(dic)
