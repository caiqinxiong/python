class Animal:
    def __init__(self,hp,ad,name):
        self.hp = hp
        self.ad = ad
        self.name = name
    def eat(self):
        print('%s执行我啦'%self.name)
        self.hp += 5

class Person(Animal):
    def __init__(self,name,hp,ad,sex,job):
        self.sex = sex    # 人特有的
        self.job = job    # 人特有的
        Animal.__init__(self, hp, ad, name)
    def attack(self,dog):
        dog.hp -= self.ad
        print('%s攻击了%s,%s掉了%s点血'%(self.name,dog.name,dog.name,self.ad))

class Dog(Animal):
    def __init__(self,name,kind,hp,ad):   # 初始化方法
        Animal.__init__(self,hp,ad,name)
        self.kind = kind  # kind是狗特有的
    def bite(self,person):
        person.hp -= self.ad
        print('%s咬了%s,%s掉了%s点血'%(self.name,person.name,person.name,self.ad))

二饼 = Dog('二饼','哈士奇',3000,150)
print(二饼.__dict__)
alex = Person('alex',100,5,'不详','乞丐')
print(alex.__dict__)


# A和B类都需要调用相同的方法
# 创建父类C,把相同的方法放到C类中
# A和B继承C A(C)  B(C)
# A的对象和B的对象就可以直接调用C中的方法了

# A和B中有相同的方法,一部分功能相同,还有不同的部分
# 创建父类C, 把相同的部分放到C类的方法中
# 在A\B中保留不同的部分,
# 然后分别在A\B中调用C类的方法即可