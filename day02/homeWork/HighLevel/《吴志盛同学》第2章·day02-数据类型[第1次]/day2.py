购物车
1. 用户先给自己的账户充钱：比如先充3000元。
2. 页面显示 序号 + 商品名称 + 商品价格，如：
        1 电脑 1999 
        2 鼠标 10
        …
        n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5. 用户输n入为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
6. 用户输入Q或者q退出程序。
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
wallet = int(input("请输入您的总资产："))
while True:
    print("下面是商品展示：")
    commodity = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "键盘", "price": 50},
        {"name": "内存条", "price": 100},
    ]

    for n1 in range(len(commodity)):
        print(n1 + 1, commodity[n1]["name"], commodity[n1]["price"])
    user_list = {}
    sum = 0
    while True:
        nu1 = input("请输入商品序号,退出请按Q|q）：").upper()
        if nu1 == "Q":
            break
        else:
            nu2 = input("输入选择的商品的数量：")
            user_list[nu1] = nu2   #记录商品序号和份数
            print("您购买的{}，数量为{}".format(commodity[int(nu1) - 1]["name"], nu2))
            sum1 = commodity[int(nu1) - 1]["price"] * int(nu2)
            sum = sum + sum1

    print("购买商品总花费为：" + str(sum))
    if sum <= int(wallet):
        print("购买成功！您的资产剩余为：{}".format((int(wallet) - sum)))
    else:
        print("余额不足，购买失败！")
    wallet = wallet - sum
    assure = input("继续购买请输Y，N退出：").upper()
    if assure == "N":
        break


1、有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
#1)
print(name.lstrip())
#2)
print (name[2:])
#3)
print (name[:-2])
#4)
print(name[1:-1])
#5)
print(name.startswith('al'))
#6)
print(name.endswith('Nb'))
#7)
print(name.replace('l','p'))
#8)
print(name.replace('l','p',1))
#9)
print(name.split('l'))
#10)
print(name.split('l',1))
#11)
print(name.upper())
#12)
print(name.lower())
#13)
print(name.capitalize())
#14)
print(name.count('l'))
#15)
print(name[:4].count('l'))
#16)
print(name.index('N'))
#17)
print(name.find('N'))
#18)
print(name.find('X le'))
#19)
print(name[1:2])
#20)
print(name[:3])
#21)
print(name[-2:])
#22)
print(name.find('e'))


2、有字符串s = "123a4b5c"
s = "123a4b5c"
#1)
s1=s[:3]
print(s1)
#2)
s2=s[3:6]
print (s2)
#3)
s3=s[::2]
print(s3)
#4)
s4=s[1:6:2]
print(s4)
#5)
s5=s[-1]
print (s5)
#6)
s6=s[-3::-2]
print(s6)


3、使用while或for循环分别打印字符串s="asdfer"中每个元素。
s="asdfer"
n=0
while n < len(s):
    print (s[n])
    n +=1

for i in s:
    print(i)

	
4、使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
s="asdfer"
lis=s.split()
for i in lis:
    print(i)


5、使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，
csb,...gsb。
s="abcdefg"
for i in s:
    print (i+'sb')


6、使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出
发！"。
s="321"
for i in s:
    print("倒计时"+i+"秒")
print ("出发！")

7.实现一个整数加法计算器(两个数相加)：
content = input("请输入内容:").split("+")
sum=0
for i in content:
    sum +=int(i)
print(sum)

8.
content = input("请输入内容:").split("+")
sum=0
for i in content:
    sum +=int(i)
print(sum)



9、计算用户输入的内容中有几个整数（以个位数为单位）。
content = input("请输入内容：")
int=0
for i in content:
    if i.isdigit() == True:
        int +=1
    else:
        continue
print(int)



10、写代码，完成下列需求
while True:
    chose = input("选择回家的路,请输入A,B，C：").upper()
    if chose == "A":
        print("走大路回家")
        chose1=input('选择步行还是公交车？')
        if chose1 == "步行":
            print ("20分钟到家")
            break
        elif chose1 == "公交车":
            print("10分钟到家")
            break
        else:
            print ("请您重新选择")
    elif  chose == "B":
        print("走小路回家")
        break
    elif chose == "C":
        print('绕道回家')
        chose2=input('选择游戏厅，还是网吧？')
        if chose2 == '游戏厅':
            print ('一个半小时到家，爸爸在家，拿棍等你。')
            continue
        elif chose2 == '网吧':
            print ('两个小时到家，妈妈已做好了战斗准备。')
            continue
    else:
        print("请您重新选择")
		

11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
sum1=0
sum2=0
for i in range(1,100,2):
    sum1=sum1+i
for l in range(2, 100, 2):
    if l == 88:
        continue
    sum2=sum2+l
print(sum1-sum2)


16,制作趣味模板程序需求：等待户输名字、地点、爱好，根据户的名字和爱好进任意现实
user=input('用户名：')
address=input('地点：')
hobby=input('爱好：')

information='''
敬爱可亲的%s，最喜欢在%s地%s
''' % (user,address,hobby)

print (information)


17、等待用户输入内容，检测用户输入内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重
新输入”，并允许用户重新输入并打印。敏感字符：“粉嫩”、“铁锤”
user=input('用户名：')
address=input('地点：')
hobby=input('爱好：')
information='''
敬爱可亲的%s，最喜欢在%s地%s
''' % (user,address,hobby)
word=['粉嫩','铁锤']
for i in word:
    if hobby == i:
        print('存在敏感字符请重新输入')
        continue
        print (information)

18、写代码，有如下列表，按照要求实现每一个功能		
li = ["alex", "WuSir", "ritian", "barry", "wenzhou","eric"]
#1)
print (len(li))
#2)
li.append("seven")
print(li)
#3)
li.insert(0,"Tony")
print(li)
#4)
li[1]="Kelly"
print(li)

#5)
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2=[1,"a",3,4,"heart"]
l3=li+l2
print(l3)

#7) 
li.remove("eric")
print(li)

#8)
print (li.pop(1))
print (li)

#9)待改
del li[1:3]
print (li)

#10)
li.reverse()
print(li)

#11)
print (li.count("alex"))


19、写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
#1)
l1=li[:3]
print (l1)
#2)
l2=li[3:6]
print(l2)
#3)
l3=li[::2]
print(l3)
#4)
l4=li[1:6:2]
print(l4)
#5)
l5=li[-1:]
print (l5)
#6)
l6=li[-3::-2]
print (l6)

20、写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#1)
lis[3][2][1][0]="TT"
print (lis)
lis[3][2][1][0]=lis[3][2][1][0].upper()
print(lis)
#2)
lis[1]=100
print (lis)
lis[-5]=100
print(lis)
#3)
lis[3][2][1][2]='101'
print(lis)
lis[-3][-2][-1][-1]='101'
print(lis)



21、请用代码实现：
li = ["alex", "eric", "rain"]
str='''
%s_%s_%s
''' % (li[0],li[1],li[2])
print(str)


22、利用for循环和range打印出下面列表的索引
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(len(li)):
    print(i)
	
23、利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中
li=[]
for i in range(2,100,2):
    li.append(i)
print (li)

24、利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中
li=[]
for i in range(3,50,3):
    li.append(i)
print (li)

25、利用for循环和range从100~1，倒序打印。
for i in range(100,0,-1):
    print (i)

26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛
选，将能被4整除的数留下来
	li=[]
for i in range(100,9,-2):
    li.append(i)
print (li)
for l in li:
    if l % 4 == 2:
        li.remove(l)
print (li)

26、利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改
成*
li=[]
for i in range(1,31):
    li.append(i)
print(li)
for l in range(len(li)):
    if li[l] % 3 == 0:
        li[l]="*"
print(li)

27、查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添
加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
l1=[]
l2=[]
for i in li:
    l1.append(i.strip())
for l in l1:
    if (l.startswith('A') or  l.startswith('a')) and l.endswith('c'):
         l2.append(l)
for i in l2:
    print(i)


28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
l1=[]
for i in li:
    content = input("用户评论内容：")
    if content == i:
        l1.append(content.replace(content,len(content)*"*"))
        print(l1)
        break
    else:
        l1.append(content)
        print(l1)
        break

		
29、有如下变量（tu是个元祖），请实现要求的功能
#a)
元组的元素不能修改,只能读
元组使用小括号
#b)
不可以
#c)
列表
可以
tu[1][2]['k2'].append("Seven")
print(tu[1][2]['k2'])

#d)
元组
不可以
		
		
		
		
30、字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#a)
for keys in dic.keys():
    print (keys)
#b)
for values in dic.values():
     print (values)
#c)
for keys,values in dic.items():
    print(keys,values)
#d)
dic['k4']='v4'
print (dic)
#e)
dic['k1']='alex'
print(dic)
#f)
dic['k3'].append(44)
print(dic)
#g)
dic['k3'].insert(1,18)
print(dic)


31.
av_catalog = {
"欧美":{
"www.youporn.com": ["很多免费的,世界最大的","质量一般"],
"www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
"x‐art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]},
"日韩":{
"tokyo‐hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]},
"大陆":{
"1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]}
}
#a)
av_catalog["欧美"]["www.youporn.com"].insert(1,'量很大')
print(av_catalog["欧美"])
#q)
av_catalog["欧美"]["x‐art.com"].remove( "全部收费,屌丝请绕过")
print(av_catalog["欧美"])
#c)
# av_catalog["欧美"]["x‐art.com"].remove( "全部收费,屌丝请绕过")
# print(av_catalog["欧美"])

#d)
av_catalog["日韩"]["tokyo‐hot"][1]=av_catalog["日韩"]["tokyo‐hot"][1].upper()
print(av_catalog["日韩"])

#e)
av_catalog["大陆"]['1048' ]=(['一天就封了'])
print(av_catalog["大陆"])
#f)
av_catalog["欧美"].pop("letmedothistoyou.com")
print(av_catalog["欧美"])
#g)
av_catalog["大陆"]["1024"].insert(0,"可以爬下来")
print(av_catalog["大陆"])


32.
num="k:1|k1:2|k2:3|k3:4"
lis1=num.split("|")
lis2=[]
dic={}
print (lis1)
for i in lis1:
    l=i.split(":")
    lis2.append(l)
print(lis2)
for q in lis2:
    dic[q[0]]=q[1]
print(dic)


33、元素分类
li= [11,22,33,44,55,66,77,88,99,90]
dic={'k1':[],'k2':[]}
for i in li:
    if i > 66:
         dic['k1'].append(i)
    else:
        dic['k2'].append(i)
print(dic)


