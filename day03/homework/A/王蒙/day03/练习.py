# -*- coding:utf-8 -*-
import os
import math

# 1.任一英文纯文本文件，统计其中的每个单词出现的个数
def get_wordLst():
    with open("English","r",encoding="utf-8") as f:
        word_lst=[]
        for line in f:
            line = line.strip()
            lst = line.split(" ")
            word_lst.extend(lst)
        return word_lst
def get_wordNum():
    total_word_list = get_wordLst() # 总单词表
    lst = []
    equal_word_list = [] # 相同单词表
    for word in total_word_list:
        if word not in lst:
            lst.append(word)
    for j in lst:
        for i in total_word_list:
            if j == i:
                equal_word_list.append(i)
        print(j,"==>",len(equal_word_list))
        equal_word_list.clear()
get_wordNum()

# 2、写函数，计算传入的参数和

def Sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
s = Sum(2,3,5)
print(s)

# 3、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改

def modify(file,old,new):
    with open(file,"r",encoding="utf-8") as f,open("info.bak","w",encoding="utf-8") as f2:
        # s = "王蒙"
        # s1 = "李明"
        for line in f:
            line = line.strip()
            if s in line:
                line.replace(old,new)
                f2.write(line)
                print(line)

    os.replace("info.bak",file)
modify("info","王蒙","黎明")

# 4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。

def isNone(a):
    blank = False # 为False时没有空内容
    for line in a:
        if line.isspace(): #  isspace() 方法检测字符串是否只由空格组成
            blank = True
    return blank
a=[" ","wang","me ng"]
ret = isNone(a)
print(ret)


# 5、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容（对value的值进行截断），
# 并将新内容返回给调用者，注意传入的数据可以是字符、list、dict

def Inter():
    dic = {"uname":"wangmeng","pwd":"wqzj"}
    for k,v in dic.items():
        if len(dic[k]) > 2:
            dic[k] = v[0:2]
        else:
            dic[k] = v
    return dic
Inter()

# 6、 写函数，返回一个扑克列表，里面有52项，每一项是一个元组
def poker(Num,Gra):
    total_lst = []
    for item in Num:
        for element in Gra:
            if str(item).isalpha():
                com = str(element)+str(item)
                total_lst.append((com,))
            else:
                total_lst.append((element,item))
    print(len(total_lst))
    return(total_lst)
com=poker(["A",2,3,4,5,6,7,8,9,10,"J","Q","K"],["红心","黑桃","方块","草花"])
print(com)

# 7.写入函数，出入n个参数，返回字段{"max":最大值,"min":最小值}
def Size(a,b,c,d):
    lst = [a,b,c,d]
    max = lst[0]
    min = lst[0]
    size_dic = {}
    for i in lst:
        if i > max:
            max = i
        elif i< min:
            min = i
    size_dic["最大值"] = max
    size_dic["最小值"] = min
    return size_dic
req = Size(6,10,9,1)
print(req)

# 8、写函数，专门计算图形的面积

def area(name,*args):
    def Rectangle(a,b):
        return a*b
    def Square(a):
        return a**2
    def Round(r):
        return math.pi*r*r
    if name == "圆形":
        return Round(*args)
    elif name == "正方形":
        return Square(*args)
    elif name == "长方形":
        return Rectangle(*args)

print(area("长方形",3,4))
print(area("正方形",3))
print(area("圆形",5))

# 9、阶乘
def cal(num):
    product = 1
    for i in range(num,0,-1):
        product *= i
    return(product)
pro = cal(7)
print(pro)

# 10、10、如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
{'name': 'IBM', 'shares': 100,'price': 91.1},
{'name':'AAPL','shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 使用map
comp = map(lambda y:y['shares']*y['price'],portfolio )
print(list(comp))

f = filter(lambda a:a['price']>=100,portfolio)
print(list(f))

# 11、将以a开头的元素字母改为大写字母

def func():
    li = ['alex', 'egon', 'smith', 'pizza', 'alen']
    new_lst = []
    for item in li:
        if item.startswith('a'):
            new_lst.append(item.capitalize())
        else:
            new_lst.append(item)
    return (new_lst)
print(func())

# 12、请以列表中每个元素的第二个字母倒序排序
li = ['alex','egon','smith','pizza','alen']
temp_lst = []
new_li = []
for item in li:
    for i in item[1:]:
        temp_lst.append(i)
    temp_lst.reverse()
    s =item[0]+"".join(temp_lst)
    temp_lst.clear()
    new_li.append(s)

print(new_li)


# 13、有名为poetry.txt的文件，其内容如下，请删除第三行

with open("poetry.txt","r",encoding="utf-8") as f1,open("poetry1.txt","w",encoding="utf-8") as f2:
    s = "晴川历历汉阳树，芳草萋萋鹦鹉洲。"
    for line in f1:
        line = line.strip()
        if line == s:
            continue
        else:
            f2.write("line"+"\n")
os.remove("poetry.txt")
os.rename("poetry1.txt","poetry.txt")

# 14、有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”alex”,
# 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在；

def judge():
    with open("username.txt","r+",encoding="utf-8") as f:
        uname = "alex"
        for line in f:
            line = line.strip()
            if uname == line:
                print("用户名已经存在")
                break
        else:
            f.write("\n%s" % str)
judge()

# 15、有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行
with open("user_info.txt","r") as f,open("user_info1.txt","w",encoding="utf-8") as f2:
    for line in f:
        line = line.strip()
        lst = line.split(",")
        if lst[1].strip() == "100003":
            del lst[0:]
        else:
            f2.write(",".join(lst)+"\n")
os.replace("user_info1.txt","user_info.txt")


# 16、有名为user_inf.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li；

with open("user_inf.txt","r",encoding="utf-8") as f,open("user_inf1.txt","w",encoding="utf-8") as f1:
    for line in f:
        line = line.strip()
        lst = line.split(",")
        if lst[1].strip() == "100002":
            lst[0] = "alex li"
            f1.write(",".join(lst)+"\n")
        else:
            f1.write(",".join(lst)+"\n")
os.replace("user_inf1.txt","user_inf.txt")