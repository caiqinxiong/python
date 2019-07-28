# bool值
# 数字 0 False
    # 非0 True
# 字符串 '' False
    # 非空 True
# [] tuple() {} --> False
# None --> False

lst = []
if lst:
    print(lst)
else:
    print('列表为空')