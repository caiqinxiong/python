class Studnet:
    opt_lst = [('查看可选课程', 'show_courses'),
               ('选择课程', 'choose_course'), ('查看已选课程', 'show_selected_course')
        , ('退出', 'quit')]
    def __init__(self,name):
        self.name = name
        self.courses = []
    def show_courses(self):
        print('查看一共有多少门课程')

    def choose_course(self):
        print('选择课程')

    def show_selected_course(self):
        print('查看已经选择的课程')

    def quit(self):
        print('退出')

stu = Studnet('alex')
for index,opt in enumerate(Studnet.opt_lst,1):
    print(index,opt[0])
num = int(input('请输入您要选择的操作序号:'))
if hasattr(stu,Studnet.opt_lst[num-1][1]):
    getattr(stu,Studnet.opt_lst[num-1][1])()

# 选课系统
    # 改进 反射
    # classmethod/staticmethod装饰器