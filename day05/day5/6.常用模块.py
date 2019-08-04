# 什么叫模块?
# 都是C写的
    # 大部分内置模块
    # 内置函数
# 所有的模块当中也是一堆代码
# 这一堆代码是别人写好的功能交给我们直接使用的

# 模块的分类
    # 内置模块 : 不需要你自己安装,直接就可以使用的
    # 扩展模块/第三方模块 : 需要你自己安装一下才能使用的
        # django
        # flask
        # beautifulsoup
        # pandas
    # 自定义模块

# random模块
    # 随机
    # 随机的规则 : 在某一个范围中能够抽到每一个值的概率都相同
# 本身random模块和随机之间的关系
    # 随机数 是一个概念
    # 生成随机数 处理随机数 :random模块的
import random
# ret = random.random()   # (0,1)
# print(ret)
# ret2 = random.randint(1,2) # [1,2]
# print(ret2)
# ret2 = random.randrange(1,20,2) # [1,20)
# print(ret2)
# lst = [1,2,3,4,5,6,7]
# random.shuffle(lst)
# print(lst)

# ret = random.choice([1,2,'alex',[1,2,3]])
# print(ret)

# ret = random.sample([1,2,'alex',[1,2,3]],20)
# print(ret)





