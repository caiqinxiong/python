"""
%和format的区别
http://www.cnblogs.com/liwenzhou/p/8570701.html
"""

c = (250, 250)

command1 = "二营长,向他开炮: 敌人坐标:%s" % (c, )
print(command1)

command2 = "二营长,向他开炮: 敌人坐标:{}".format(c)
print(command2)


print(f"二营长,向他开炮: 敌人坐标:{c}")

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{self.name} is {self.age} years old.".format(self=self)

p1 = Person("Alex", 9000)
print(p1)

data = [11, 22]
print("{0} --- {0}".format(data))
print("{0[0]} --- {0[0]}".format(data))
print("{0[0]} --- {0[1]}".format(data))

print("{:>10}".format(18))
print("{:0>10}".format(18))
print("{:A>10}".format(18))

print("18".zfill(10))

print("{:.4f}".format(3.1415926))

print("{:,}".format(1234567890))