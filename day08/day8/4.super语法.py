class Course:
    course_lst = []
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price

class Role:
    def __init__(self,name):
        self.name = name
    def show_course(self):
        for item in Course.course_lst:
            print(item.name,item.period,item.price)

class Student(Role):
    def __init__(self,name):
        # Role.__init__(self,name)
        # super(Student, self).__init__(name)
        super().__init__(name)   # super也可以帮助我们找到父类
        self.courses = []

class Manager(Role):pass

python = Course('python','6 months',19800)
linux = Course('linux','5 months',17800)
Course.course_lst = [python,linux]   # 所有的可选课程

m = Student('alex')
print(m.name)
m.show_course()