#!/usr/bin/env python
# coding: utf-8

"""
Created by zwb on 2018/8/23
"""


#1. 第一题
#name = "aleX leNb"

#print(name.strip())

#print(name.lstrip('al'))

#print(name.rstrip('Nb'))

#print(name.lstrip('a').rstrip('b'))

#if name.startswith('al'):
#    print("变量是以al开头")
#else:
#    print("变量不是以al开头")

#if name.endswith('Nb'):
#    print("变量是以Nb结尾")
#else:
#    print("变量不是以Nb结尾")

#print(name.replace('l', 'p'))
#print(name.replace('l', 'p', 1))

#print(name.split('l'))
#print(name.split('l', 1))

#print(name.upper())
#print(name.lower())
#print(name.capitalize())
#print(name.count('l'))
#print(name.count('l', 0, 3))
#print(name.index('N'))
#print(name.find('N'))
#print(name.find('X le'))
#print(name[1])
#print(name[0:3])
#print(name[-2:])
#print(name.find('e'))


#2. 第二题
#s = "123a4b5c"
#s1 = s[0:3]
#s2 = s[3:6]
#s3 = s[::2]
#s4 = s[1:-2:2]
#s5 = s[-1]
#s6 = s[-3:0:-2]
#print(s1)
#print(s2)
#print(s3)
#print(s4)
#print(s5)
#print(s6)

#3. 第三题
s = "asdfer"
#for i in range(len(s)):
#    print(s[i])

#4. 第四题
s = "asdfer"
#for i in s:
#    print(s)

#5. 第五题
s = "abcdefg"
#for i in range(len(s)):
#    print("{0}{1}".format(s[i], "sb"))

#6. 第六题
#s = "321"
#for i in range(len(s)):
#    print("倒计时{0}秒".format(s[i]))
#    if i == len(s)-1:
#        print("出发")

#7. 第七题
#content = input("请输入内容：")
#a = int(content.split('+')[0])
#b = int(content.split('+')[1])
#sum = a + b
#print("算数和：{0}".format(a+b))

#8. 第八题
#content = input("请输入内容：")
#line = content.split("+")
#sum = 0
#for i in range(len(line)):
#    sum += int(line[i])
#print("算数和：{0}".format(sum))

#9. 第九题
#content = input("请输入内容：")
#j = 0
#for i in range(len(content)):
#    str = content[i]
#    if  str.isdigit():
#        j += 1
#print("用户输入的内容中有{0}个整数".format(j))

#10. 第十题
#while True:
#    msg_A = "A|B|C"
#    msg_A_1 = "公交车|步行"
#    msg_B = "游戏厅|网吧"
#    content = input("{0}\n请输入您的选择:".format(msg_A))
#    if content == 'A':
#        print("走大路回家")
#        content = input("{0}\n请继续您的选择:".format(msg_A_1))
#        if content == "公交车":
#            print("10分钟到家")
#            break
#        elif content == "步行":
#            print("20分钟到家")
#            break
#    elif content == 'B':
#        print("走小路回家")
#        break
#    elif content == 'C':
#        print("绕道回家")
#        content = input("{0}\n请继续您的选择:".format(msg_B))
#        if content == "游戏厅":
#            print("一个半小时到家，爸爸在家，拿棍等你")
#            continue
#        elif content == "网吧":
#            print("两个小时到家，妈妈已做好战斗准备")
#            continue

#11. 第十一题
#i = 0
#sum = 0
#while i < 100:
#    if i == 88:
#        i += 1
#        continue
#    elif i%2 == 0:
#        sum -= i
#    elif i%2 != 0:
#        sum += i
#    i += 1
#print("sum: {0}".format(sum))

#16. 第十六题
#username = input("请输入您的名字：")
#sit = input("请输入您的地点：")
#hobby = input("请输入您的爱好：")
#
#print("敬爱可亲的{0},最喜欢在{1}{2}".format(username, sit, hobby))

#17. 第十七题
#keyword = ["粉嫩", "铁锤"]
#while True:
#   content = input("请输入您需要查询的关键字：")
#   if content in keyword:
#       print("存在敏感字符请重新输入")
#   else:
#       print("查询到结果如下：1.xxx\n2.xxx")
#       break


#18. 第十八题
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#print(len(li))

#li.append("seven")

#li.insert(0, "Tony")

#li[1] = "Kelly"

#l2 = [1, "a", 3, 4, "heart"]
#li.extend(l2)

#s = "qwert"
#li.extend(s)

#li.remove("eric")

#del_str = li[1]
#li.pop(1)
#print("删除元素：{0}, 删除后列表：{1}".format(del_str, li))

#str1, str2, str3 = li[1:4]
#li.remove(str1)
#li.remove(str2)
#li.remove(str3)
#print("删除元素：{0} {1} {2}, 删除后列表： {3}".format(str1, str2, str3, li))


#li.reverse()

#count = li.count("alex")
#print(count)


#19. 第十九题
li = [1, 3, 2, "a", 4, "b", 5, "c"]
#li = li[0:3]

#li = li[3:6]

#li = li[::2]

#li = li[1:-1:2]

#li = li[-1]

#li = li[-3:0:-2]

#print(li)


#20. 第二十题
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#lis[3][2][1][0] = lis[3][2][1][0].upper()
#lis[1] = lis[3][2][1][1] = "100"
#lis[3][2][1][2] = 101
#print(lis)

#21. 第二十一题
#li = ["alex", "eric", "rain"]
#print("_".join(li))

#22. 第二十二题
#li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#for i in range(len(li)):
#    print(i)

#23. 第二十三题
#lis = []
#for i in range(101):
#    if i % 2 == 0:
#        lis.append(i)
#print(lis)

#24. 第二十四题
#lis = []
#for i in range(50):
#    if i % 3 == 0:
#        lis.append(i)
#print(lis)

#25. 第二十五题
#lis = [x for x in range(101)]
#lis.reverse()
#for i in lis:
#    print(i)


#26. 第二十六题
#lis = [x for x in range(10, 101)]
#lis.reverse()
#lis1 = []
#for i in lis:
#    if i % 2 == 0:
#        lis1.append(i)
#
#for i in lis1:
#    if i % 4 != 0:
#        lis1.remove(i)
#print(lis1)

#27. 第二十七题
#lis = [ x for x in range(1, 31)]
#j = 0
#for i in lis:
#    if i % 3 == 0:
#        lis[j] = '*'
#    j += 1
#print(lis)

#28. 第二十八题
#li = ["TaiBai", "alexC", "AbC", "egon", " riTiAn", "WuSir", " aqc"]
#new_lis = []
#for i in range(len(li)):
#    li[i] = li[i].strip()
#    if (li[i].startswith("A") and li[i].endswith("c")) or (li[i].startswith("a")
#        and li[i].endswith("c")):
#        new_lis.append(li[i])
#print(new_lis)

#29. 第二十九题
#li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
#lis = []
#while True:
#    content = input("请输入您的评论内容: ")
#    for i in li:
#        if i in content:
#            content = content.replace(i, "*"*len(i))
#    lis.append(content)
#    print(lis)

#30. 第三十题
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)},
               44])

#1.
#元组被称为只读列表，即数据可以被查询，但不能被修改
#
#2.
#第一个元素"alex不可修改"
#
#3.
#"k2" 对应的值是列表类型，可修改
#tu[1][2]["k2"].append("Seven")
#print(tu)

#4.
#"k3"对应的值得类型是元组，不可修改


#31. 第三十一题
dic = {"k1": "v1", "k2": "v2", "k3": [11,22,33]}

#for k in dic:
#    print(k)

#for k in dic:
#    print(dic[k])

#for k in dic:
#    print(k, dic[k])

#dic['k4'] = "v4"

#dic["k1"] = "alex"

#dic["k3"].append(44)

#dic["k3"].insert(0, 18)
#print(dic)

#32. 第三十二题
#av_catalog['欧美']['www.youporn.com'].insert(1, "量很大")
#av_catalog['欧美']['www.x-art.com'].pop(1)
#av_catalog['日韩']['tokyo-hot'][1] = av_catalog['日韩']['tokyo-hot'][1].upper()
#av_catalog['大陆']['1048'] = ["一天就封了"]
#del av_catalog['欧美']['letmedothistoyou.com']
#av_catalog['大陆']['1024'][0] = av_catalog['大陆']['1024'] + "可以爬下来"


#33. 第三十三题
#s = "k:1|k1:2|k2:3|k3:4"
#dic = {}
#s = s.split("|")
#for i in s:
#    k = i.split(":")[0]
#    v = int(i.split(":")[1])
#    dic[k] = v
#print(dic)

#34. 第三十四题
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {}
k1 = []
k2 = []
for i in li:
    if i > 66:
        k1.append(i)
    elif i < 66:
        k2.append(i)
dic[str(k1)] = "大于66的所有值列表"
dic[str(k2)] = "小于66的所有值列表"
print(dic)

