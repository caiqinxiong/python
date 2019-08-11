import re
# 1.其他的方法
# 1[2-9]\d{9} 11位手机号码
# 所有的正则表达式在工具中如果匹配成功,直接放到r''里就可以直接使用
# phone_num = input('请输入合法的手机号:')
# regex = r'^1[2-9]\d{9}$'
# ret = re.findall(regex,phone_num)
# print(ret)
#
# phone_num = input('请输入合法的手机号:')
# regex = r'^1[2-9]\d{9}$'
# ret = re.search(regex,phone_num)
# if ret:
#     print('是合法的手机号码 %s'%phone_num)
# else:
#     print('不是合法的手机号码')

# match
# ret = re.search(r'\d+',r'alex84')   # 从头开始往后找任何地方有符合条件的都返回一个
# print(ret)
# ret = re.match(r'\d+',r'84alex')   # 从头开始匹配,如果开始部分匹配到了就是匹配成功,如果开始部分没匹配到,就匹配失败
# print(ret)   # 表示没有匹配到
# phone_num = input('请输入合法的手机号:')
# regex = r'1[2-9]\d{9}$'
# ret = re.match(regex,phone_num)
# if ret:
#     print(ret)
#     print('是合法的手机号码 %s'%phone_num)
# else:
#     print('不是合法的手机号码')

# split
# s = 'alex|84|'
# lst = s.split('|')
# print(lst)

# ret = re.split(r'\d+',r'alex84wusir73')
# print(ret)

# sub  替换方法
# ret = re.sub(r'\d+','H','eva123alex456',1)
# print(ret)
# subn
# ret = re.subn(r'\d+','H','eva123alex456')
# print(ret)

# 1.数据安全
# 2.用户体验
# 3.空间成本   迅雷:下载电影 5g的电影
# 4.时间成本   计算器: 表达式的计算时间

# compile 预编译 预先来编译一下我们写好的正则
# rule = re.compile('\d+')
# ret = rule.findall('alex123eva456')
# print(ret)
# ret = rule.findall('手机号码13737373377\n身份证号 110107197712072277')
# print(ret)
# '\d+' -- > 程序就去做对应的匹配了呢?
# 程序就要先解析你的正则表达式
# 你的需求是连续的任意数字
# 循环你的字符串,找到对应你需求的内容,开始匹配返回结果

# finditer
# ret = re.findall('\d','alex1916936916598sb7985073495898632847')
# print(ret)
# ret = re.finditer('\d','alex1916936916598sb7985073495898632847')
# print(ret)
# for i in ret:
#     print(i.group())

# 2.再分析 findall \search 和分组的关系
# ret = re.findall('\d(\d)','a1,b22,c345')
# print(ret)  # [2,4]
# ret = re.findall('\d(?:\d)','a1,b22,c345')
# print(ret)  # ['22', '34']

# ret = re.search('(?P<num1>\d)(?P<num2>\d)','a14,b22,c3357')
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group('num1'))
# print(ret.group('num2'))

# ret = re.search('(?P<num1>\d)(?P=num1)','a14,b22,c3357')
# print(ret.group())

# 3.分组的作用
# import re
# ret = re.search("<(?P<tag_name>\w+)>.*</(?P=tag_name)>", "<h1>hello</h1>")
# print(ret)  # 结果 ：h1
# print(ret.group('tag_name'))  # 结果 ：h1
# print(ret.group())  # 结果 ：<h1>hello</h1>

    # 为什么findall要优先显示分组中的内容呢?
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# lst= list(filter(lambda n:'.' not in n ,ret))
# print(lst)
# 相匹配的内容的正则比较简单,但是不想匹配的内容也会被简单的正则匹配出来
# 怎么办呢?
# 只能把不想要的先匹配出来

# 4.再看一些练习题

