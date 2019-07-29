#python27期 罗锋
#有1个列表 l=[2,4,6,7,8,10,122,234,23,34,56,29,]
l=[2,4,6,7,8,10,122,234,23,34,56,29]
def func(l,num):
    mid = (len(l) - 1) // 2
    l=sorted(l)
    if l:
        if num > l[mid]:
            func(l[mid+1:],num)
        elif num < l[mid]:
            func(l[:mid],num)
        elif num == l[mid]:
            print(mid)
    else:
        print('找不到这个数')
func(l,56)
