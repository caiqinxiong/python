
import random
N=''
for i in range(6):
    nume=random.randrange(0,6)              #生成随机数与循环次数比对   0-6位之间
    nume1 = random.randrange(0,6)
    if  nume == i:
        tmp=chr(random.randint(65,90))
    elif nume1 == i:
        tmp = chr(random.randint(97,122))
    else:
        tmp=random.randint(0,9)
    N+=str(tmp)
print(N)