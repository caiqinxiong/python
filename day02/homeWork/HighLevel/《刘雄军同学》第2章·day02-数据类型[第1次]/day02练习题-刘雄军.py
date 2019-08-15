#练习题：
# 1、有变量name = "aleX leNb"完成如下操作：
# 1)  移除name变量对应的值两边的空格, 并输出处理结果
# name = "aleX leNb"
# name1 = name.strip()
# print(name1)

# 2)  移除name变量左边的"al"并输出处理结果
# name = "aleX leNb"
# name1 = name.strip('al')
# print(name1)

# 3)  移除name变量右面的"Nb", 并输出处理结果
# name = "aleX leNb"
# name1 = name.strip('Nb')
# print(name1)

# 4)  移除name变量开头的a"与最后的"b",并输出处理结果
# name = "aleX leNb"
# name1 = name[1:-1]
# print(name1)

# 5)  判断 name 变量是否以 "al" 开头,并输出结果
# name = "aleX leNb"
# name1 = name.startswith('al')
# print(name1)

# 6)  判断name变量是否以"Nb"结尾,并输出结果
# name = "aleX leNb"
# name1 = name.endswith('Nb')
# print(name1)

# 7)  将 name 变量对应的值中的所有的"l" 替换为 "p",并输出结果
# name = "aleX leNb"
# name1 = name.replace('l','p')
# print(name1)

# 8)  将name变量对应的值中的第一个"l"替换成"p",并输出结果
# name = "aleX leNb"
# name1 = name.replace('l','p',1)
# print(name1)

# 9)  将 name 变量对应的值根据所有的"l" 分割,并输出结果。
# name = "aleX leNb"
# name1 = name.split('l')
# print(name1)

# 10) 将name变量对应的值根据第一个"l"分割,并输出结果。
# name = "aleX leNb"
# name1 = name.split('l',1)
# print(name1)

# 11) 将 name 变量对应的值变大写,并输出结果
# name = "aleX leNb"
# name1 = name.upper()
# print(name1)

# 12) 将 name 变量对应的值变小写,并输出结果
# name = "aleX leNb"
# name1 = name.lower()
# print(name1)

# 13) 将name变量对应的值首字母"a"大写,并输出结果
# name = "aleX leNb"
# name1 = name.capitalize()
# print(name1)

# 14) 判断name变量对应的值字母"l"出现几次，并输出结果
# name = "aleX leNb"
# name1 = name.count('l')
# print(name1)

# 15) 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# name = "aleX leNb"
# name1 = name.count('l',4)
# print(name1)

# 16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
# name = "aleX leNb"
# name1 = name.index('N')
# print(name1)

# 17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回‐1)输出结果
# name = "aleX leNb"
# name1 = name.find('N')
# print(name1)

# 18) 从name变量对应的值中找到"X le"对应的索引,并输出结果
# name = "aleX leNb"
# name1 = name.find('X le')
# print(name1)

# 19) 请输出 name 变量对应的值的第 2 个字符?
# name = "aleX leNb"
# name1 = name[1]
# print(name1)

# 20) 请输出 name 变量对应的值的前 3 个字符?
# name = "aleX leNb"
# name1 = name[:3]
# print(name1)

# 21) 请输出 name 变量对应的值的后 2 个字符?
# name = "aleX leNb"
# # name1 = name[-2:]
# # print(name1)

# 22) 请输出 name 变量对应的值中 "e" 所在索引位置?
name = "aleX leNb"
#方法一：
# i = 0
# while 1:
#     name1 = name.find('e', i) #从下标i开始，在字符串name里查找第一个出现的字符"e"的索引位置
#     if name1 >= 0:
#         i = name1 + 1
#         print(name1)
#     else:
#         break
#方法二：
# a = 0
# for i in name:
#     if i == 'e':
#         print(a)
#     a += 1

# 2、有字符串s = "123a4b5c"
# 1)通过对s切片形成新的字符串s1,s1 = "123"
# s = "123a4b5c"
# s1 = s[:3]
# print(s1)

# 2)通过对s切片形成新的字符串s2,s2 = "a4b"
# s = "123a4b5c"
# s2 = s[3:6]
# print(s2)

# 3)通过对s切片形成新的字符串s3,s3 = "1345"
# s = "123a4b5c"
# s3 = s[::2]
# print(s3)

# 4)通过对s切片形成字符串s4,s4 = "2ab"
# s = "123a4b5c"
# s4 = s[1:-2:2]
# print(s4)

# 5)通过对s切片形成字符串s5,s5 = "c"
# s = "123a4b5c"
# s5 = s[-1]
# print(s5)

# 6)通过对s切片形成字符串s6,s6 = "ba2"
# s = "123a4b5c"
# s6 = s[-3::-2]
# print(s6)


# 3、使用while或for循环分别打印字符串s="asdfer"中每个元素。
#第一种方式whlie循环
# s="asdfer"
# i = 0
# while i < len(s):
#     s1 = s[i]
#     i += 1
#     print(s1)

#第二种方式for循环
# s="asdfer"
# for i in s:
#     print(i)

# 4、使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
# s="asdfer"
# for i in s:
#     print(s)

# 5、使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb，例如：asb, bsb，csb,...gsb。
# s="abcdefg"
# for i in s:
#     print(i+'sb,',end='')

# 6、使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s="321"
# for i in s:
#     print('倒计时{}秒'.format(i))
# else:
#     print('出发！')

# 7、实现一个整数加法计算器(两个数相加)：如：content = input("请输入内容: ") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# content = input("请输入数字: ").strip().split('+')
# sum = int(content[0]) + int(content[1])
# print(sum)

# 8、升级题：实现一个整数加法计算器（多个数相加）：如：content = input("请输入内容:")用户输入：5 + 9 + 6 + 12 + 13，然后进行分割再进行计算。
# content = input("请输入数字: ").strip().split('+')
# sum = 0
# for i in content:
#     sum += int(i)
# print(sum)

#9、计算用户输入的内容中有几个整数（以个位数为单位）如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
# content = input("请输入内容：")
# sum = 0
# for i in content:
#     if i.isdigit():
#         sum += 1
# print(sum)

#10、写代码，完成下列需求：
    # 用户可持续输入（用while循环），用户使用的情况：
    # 输入A，则显示走大路回家，然后在让用户进一步选择：
    # 是选择公交车，还是步行？
    # 选择公交车，显示10分钟到家，并退出整个程序。
    # 选择步行，显示20分钟到家，并退出整个程序。
    # 输入B，则显示走小路回家，并退出整个程序。
    # 输入C，则显示绕道回家，然后在让用户进一步选择：
    # 是选择游戏厅玩会，还是网吧？
    # 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
    # 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
# while 1:
#     content = input('请选择输入A或B或C:').strip().upper()
#     if content == 'A':
#         print('走大路回家')
#         inp1 = input('请选择公交车，还是步行？A:公交车,B:步行').strip().upper()
#         if inp1 == 'A':
#             print('10分钟到家')
#             break
#         elif inp1 == 'B':
#             print('20分钟到家')
#             break
#     elif content == 'B':
#         print('走小路回家')
#         break
#     elif content == 'C':
#         print('绕道回家')
#         inp2 = input('请选择游戏厅玩会，还是网吧？A:游戏厅,B:网吧').strip().upper()
#         if inp2 == 'A':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#         elif inp2 == 'B':
#             print('两个小时到家，妈妈已做好了战斗准备')



