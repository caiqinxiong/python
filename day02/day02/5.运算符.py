# print('='*20)
# print('-'*20)
# print('*'*20)
# print('hello,'+'world')
# s = 'hello,'+'world'
# print(s)

# a1 = input('红球1 :')
# a2 = input('红球2 :')
# print(a1 == a2)
# print(a1 != a2)

# 赋值运算 =的优先级最低
# a = 1+2-3*4/5

# a = 0
# a += 1   # a = a+1
# a -= 1   # a = a-1

# 练习题：
# a = 1
# b = 2
# a += b   # a = a+b = 1+2 = 3
# b += a   # b = b+a = 2+3 = 5
# print(a,b) # 3,5

# a = 10
# b = 6
# a %= b  #a = a%b = 4
# print(a>b)
# print(a<b)
# print(a,b)


# 逻辑运算符
# and 表示并且
    # True and True == True
    # True and False == False
# or 表示或者
    # True or True = True
    # True or False = True
    # False or True = True
    # False or False = False
# not 表示相反
    # not True == False
    # not False == True

# a = 10
# b = 5
# a<b and b>3   # False and True = False
# a<b or b>3   # False or True = True
# not a<b      # not False = True

# not a<b or a<b and b>3
# 括号的优先级最高
# not
# and
# or

# a = 10
# b = 5
# print(not a<b or a<b and b>3)
# True or False and True
# True or False
# True


# 面试题可能会遇到
# print(1 or 5)  # 1
# print(0 or 5)  # 5
# a or b # if a is True 结果是a 否则结果是b

# print(1 and 5)  # 5
# print(0 and 5)  # 0
# and和or的结果刚好相反
# print(3>4 and 5<7 or 8 and not False)

# 身份运算符
a = 1
b = 1
print(a==b)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)