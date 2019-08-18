# 程序中有多少个角色
# 每个角色有什么技能 有什么属性
# 所有的角色都是由一个模板创建的
# 我们甚至不关心程序的结果是什么

# 所有的属性 和 技能都 待在自己的角色模板中
# 能够一眼就看出程序的结构 -- 可读性好
# 能够更加方便的为角色添加技能或者属性  -- 可扩展性高

# 抽象
# 类 -- 角色模板 抽象的
# 通过类创建 对象 -- 角色 具体的
# 具体表现在所有的属性都具有了具体的值

# class 类
# def psersonType

class Person:
    def __init__(self,name,hp,ad,sex,job):
       self.username = name
       self.hp = hp
       self.ad = ad
       self.sex = sex
       self.job = job

alex = Person('alex',100,5,'不详','乞丐')   # 实例化
wusir = Person('wusir',200,6,'女','嫂子')
print('-->',alex)
print(alex.username,wusir.username)
print(alex.ad)
print(alex.sex)
print(alex.job)

# class后面跟类名创造一个类
# 类名() -->对象
class Dog:
   def __init__(self,name,kind,hp,ad):   # 初始化方法
      self.name = name
      self.kind = kind
      self.hp = hp
      self.ad = ad

旺财 = Dog('旺财','teddy',2000,300)




