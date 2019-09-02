import os
import sys
import pickle
# 教会你使用 把所有的代码整合在一起 重要的！！！
class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

class Student:
    opt_lst = [('查看所有课程', 'show_course'), ('选择课程', 'choose_course'),
               ('查看已选课程','show_selected_course'),('退出','quit')]
    def __init__(self,name):
        self.name = name
        self.courses = []    # 空列表

    def show_course(self):
        n = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s %s %s'%(n,obj.name,obj.price,obj.period))
                    n+=1
                except EOFError:
                    print('-'*50)
                    break

    def choose_course(self):
        self.show_course()
        num = int(input('请输入要选择的课程序号: '))
        # 2 怎么通过1找到对应的课程对象呢？
        n = 1
        with open('course_info',mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if n == num:   # 当前的这个obj就是我们要选择的课程对象
                        self.courses.append(obj)
                        break
                    n += 1
                except EOFError:
                    print('没有您要选择的课程')
        # 我们现在已经找到了用户要选择的课程，并且在内存中对courses列表进行了修改，但并没有把数据记录在文件里
        # 把数据记录在文件中
        with open('student_info',mode = 'rb') as f1,open('userinfo2',mode = 'wb') as f2:
            with open('student_info', 'rb') as f:
                while True:
                    try:
                        obj = pickle.load(f1)
                        if obj.name == self.name:
                            # obj = self
                            obj.courses.extend(self.courses)
                            # self.courses = []
                        pickle.dump(obj,f2)
                    except EOFError:
                        break
        os.remove('student_info')
        os.rename('userinfo2','student_info')

    def show_selected_course(self):
        with open('student_info',mode = 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.name == self.name:
                        print(obj.courses)
                        print(self.courses)
                        print([course.name for course in obj.courses])
                except EOFError:
                    break

    def quit(self):
        exit()

class Manager:
    opt_lst = [('创建学生', 'create_student'), ('创建课程', 'create_course'),
                   ('查看所有学生','show_students'),('查看所有课程','show_course'),
                   ('查看学生所选课程','show_stu_course'),('退出','quit')]
    def __init__(self,name):
        self.name = name

    def create_course(self):
        # 输入课程的信息：课程名，价格，周期
        cname = input('课程名称: ')
        cprice = input('课程价格: ')
        cperiod = input('课程周期: ')
        course = Course(cname,cprice,cperiod)
        with open('course_info',mode='ab') as f:
            pickle.dump(course,f)

    def create_student(self):
        # 为了之后学生可以进行登录、输入用户名和密码
        username = input('新用户名: ')
        password = input('新用户密码: ')
        # 把用户名和密码 、身份写入到userinfo文件里
        with open('userinfo',mode = 'a',encoding='utf-8') as f:
            f.write('%s|%s|Student\n'%(username,password))
        # 考虑这个用户是否之前登录过 -- 进阶需求
        # 这个被创建出来的学生 除了被保存在userinfo文件中，是否还应该再存储一些其他信息呢？
        # 为什么一个学生选完课程之后再次登陆能够看到学生选过的课程 -- 学生的选课情况要被保留下来
        stu = Student(username)
        with open('student_info',mode = 'ab') as f:
            pickle.dump(stu,f)

    def show_students(self):
        # 如何查看所有学生？
        # 读取student_info
        n = 1
        with open('student_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s'%(n,obj.name))
                    n+=1
                except EOFError:
                    print('-'*50)
                    break

    def show_course(self):
        n = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s %s %s %s'%(n,obj.name,obj.price,obj.period))
                    n+=1
                except EOFError:
                    print('-'*50)
                    break

    def show_stu_course(self):
        print('查看学生所选择的课程')

    def quit(self):
        exit()

username = input('请输入用户名 : ').strip()
password = input('请输入密  码 : ').strip()
flag = False
with open('userinfo',encoding='utf-8') as f:
    for line in f:
        name,pwd,ident = line.strip().split('|')  # name 用户名,pwd 密码,ident 身份(学生或者管理员)
        if username == name and password == pwd:
            print('%s用户登录成功'%ident)
            flag = True
            break    # 如果文件有100行，第一行就找到了正确的用户名和密码，不写break后99行仍然要执行for循环里的代码
    else:
        print('登录失败')
while flag:   # flag为真表示登录成功
    cls = getattr(sys.modules[__name__],ident)   # cls = Student类的地址/Manager类的地址
    obj = cls(username)                          # obj = Student的对象/Manager的对象
    for index, opt in enumerate(cls.opt_lst, 1):
        print(index,opt[0])
    num = int(input('请选择要操作的序号:'))
    getattr(obj, cls.opt_lst[num - 1][1])()
# 开发具体的功能
    # 1.从管理员的功能开始
    # 2.先完成创建工作
    # 3.再完成查看工作
# 学生用户在登录的时候
    # 每一次都要重新实例化 ： line 151行
    # 实例化的时候会创建新列表self.courses : line:16
    # 每一次选择课程需要对sel.courses进行修改 ：line40
    # 而在进行过一次选课之后，self.courses 和 文件中读出来的couses就不一致了
# 这个问题怎么去解决 ？ 本周的任务
# 立立
# 1.第一次登陆的时候 ：创建一个空对象
# self.name = '立立'
# self.courses = []  # 空列表
# 2.立立选课了
# self.courses = [python ,linux]
# 把列表记录到文件里了
# 3.立立退出了
# 4.立立第二次登录：又创建一个空对象
# self.name = '立立'
# self.courses = []  # 空列表
# 5.立立再选课
# self.courses = [go]
# 把列表记录到文件里的只有go课程了，之前选择的python和linux没了
# 期望目的：立立选择了go课程，要把go课程追加到之前已选择的课表里
# 第一：看懂分享的代码
# 第二：解决目前的问题
# 第三：代码优化
# 第四：文件的拆分
