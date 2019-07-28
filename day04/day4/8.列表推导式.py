# l = [1,2,3,4,5]
# ls = []
# for i in l:
#     ls.append(i*2)
# print(ls)
# ls = [i*2 for i in l]
# print(ls)

# l = [1,2,3,4,5]
# 所有的偶数都放到新的列表中
# ls = [i for i in range(100) if i%2 == 0]
# print(ls)

# 练习1:30以内所有能被3整除的数
# ls = [i for i in range(30) if i%3 == 0]
# print(ls)
# 练习2:30以内所有能被3整除的数的平方
# ls = [i*i for i in range(30) if i%3 == 0]
# print(ls)

# 找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# print('alexander'.count('e'))
# print('alexander'.count('n'))
# ls = [name for lst in names for name in lst if name.count('e') == 2]
# print(ls)

