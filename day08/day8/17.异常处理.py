opt_lst = [1,2,3,4]
try:
    num  = int(input('请输入序号 :'))
    print(opt_lst[num-1])
except ValueError:
    print('请输入一个数字')
except IndexError:
    print('请输入1-4之间的数字')
