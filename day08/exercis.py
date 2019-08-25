# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/8/25 上午9:11
class Course:
    course_list = []
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

class Role:
    def __init__(self,name):
        self.name = name

    def show_cours(self):
        for item in Course.course_list:
            print(item.name,item.price,item.period)


class Students(Role):
    def __init__(self,name):
        super(Students,self).__init__(name)
        self.course = []


class Manager(Role):
    def __init__(self,name):
        super(Manager,self).__init__(name)



if __name__ == '__main__':
    python = Course('python',19800,'6 month')
    linux = Course('linux', 11800,'5 month')
    Course.course_list = [python,linux]

    s = Students('caiqinxiong')
    print(s.name)
    s.show_cours()
