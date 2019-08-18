class Person:
    def __init__(self,name,hp,ad,sex,job):
       self.username = name
       self.hp = hp
       self.ad = ad
       self.sex = sex
       self.job = job
    def attack(self,dog):
        dog.hp -= self.ad
        print('%s攻击了%s,%s掉了%s点血'%(self.username,dog.name,dog.name,self.ad))

class Dog:
    def __init__(self,name,kind,hp,ad):   # 初始化方法
      self.name = name
      self.kind = kind
      self.hp = hp
      self.ad = ad
    def bite(self,person):
        person.hp -= self.ad
        print('%s咬了%s,%s掉了%s点血'%(self.name,person.username,person.username,self.ad))    # 谁在类的外部调用了这个方法,方法中的第一个self参数就是谁
alex = Person('alex',100,5,'不详','乞丐')
旺财 = Dog('旺财','teddy',2000,300)
二饼 = Dog('二饼','哈士奇',10000,500)
二饼.bite(alex)     # Dog.bite(二饼,alex)
print(alex.hp)
# 旺财.bite()     # Dog.bite(旺财)

alex.attack(旺财)
print(旺财.hp)


# 类和对象的内存解析

