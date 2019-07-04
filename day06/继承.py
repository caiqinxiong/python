# -*- coding:utf-8 -*-
# Author:caiqinxiong
class SchoolMember(object):
    members = 0  # 初始学校人数为0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
        self.name, SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


class Teacher(SchoolMember):
    def __init__(self, name, age, course, salary):
        #super(Teacher, self).__init__(name, age)
        SchoolMember.__init__(self,name,age)
        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):
    def __init__(self, name, age, grade, sid):
        super(Student, self).__init__(name, age)
        self.grade = grade
        self.sid = sid
        self.enroll()

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)


if __name__ == '__main__':
    t1 = Teacher("Alex", 22, 'Python', 20000)
    t2 = Teacher("TengLan", 29, 'Linux', 3000)

    s1 = Student("Qinghua", 24, "Python S12", 1483)
    s2 = Student("SanJiang", 26, "Python S12", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()
    s1.tell()