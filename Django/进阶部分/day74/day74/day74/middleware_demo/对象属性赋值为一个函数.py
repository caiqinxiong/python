


class Person(object):
    def __init__(self, name):
        self.name = name


p = Person("赵导")

def bo():
    print("bo~~~~~~~")

p.fangpi = bo

p.fangpi()