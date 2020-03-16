class Classes:
    def __init__(self, name):
        self.name = name
        self.students = []


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "< {} >".format(self.name)
    #
    # __str__ = __repr__


s1 = Student('洋洋')
s2 = Student('史洋洋')

c1 = Classes('s18')
c1.students.append(s1)
c1.students.append(s2)
# print(s1)
# print(s2)
# a = str(s1)
# print(a)
print(c1.students)
