#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/3'

from conf import settings
from core.combination import Combination
from core.warpper import format_wrapper

class User(Combination):
    '''基础登陆注册类,继承组合类，常用功能'''

    # 功能列表
    user_list = [
        ('登陆','login'),
        ('注册','register'),
        ('退出','quit'),
    ]

    def __init__(self,sk):
        '''
        初始化函数
        :param sk: 连接对象
        '''
        self.flag = False # 用户登陆flag
        self.conn = sk

    @format_wrapper
    def login(self):
        '''用户登陆'''
        user, pwd = input('Please input \033[31mLogin_user\033[0m >>: ').strip(), input('Please input \033[31mLogin_Password\033[0m >>: ').strip()
        user_dict = {'cmd':'login','user':user,'pwd':pwd}
        self.send_messages(user_dict)  # 发送登陆指令及信息
        recv_code = self.recv_messages() # 接受服务端的返回值
        if recv_code['code'] == 203:  # 根据服务端返回值 进行打印
            print(user,settings.code[recv_code['code']])
            self.flag = True  # flag等于true，表示登陆成功
        if recv_code['code'] == 204:
            print(user,settings.code[recv_code['code']]) # 登陆失败

    @format_wrapper
    def register(self):
        '''用户注册'''
        register_user,register_pwd = input('注册用户：').strip(),input('注册密码：').strip()
        register_dict = {'cmd':'register','register_user':register_user,'register_pwd':register_pwd} # 信息字典
        self.send_messages(register_dict)  # 发送给服务端
        recv_code = self.recv_messages()   # 接受返回值
        print(register_user,settings.code[recv_code['code']]) # 打印返回值带来的信息

