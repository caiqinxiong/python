# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 10:37
import pickle
import hashlib

from conf import settings as ss


class Certification(object):
    '''登录认证类'''

    def __init__(self):
        pass

    def written_information(self, file_name, content, mode='ab'):
        '''写入信息'''
        with open('%s' % file_name, mode='%s' % mode) as f:
            pickle.dump(content, f)


    def read_information(self, file_name):
        '''读取信息'''
        try:
            with open('%s' % file_name, mode='rb') as f:
                while True:
                    try:
                        r = pickle.load(f)
                        for k, v in r.__dict__.items():
                            yield k, v  # 以迭代器方式返回，节省内存使用
                    except EOFError:
                        break
        except:
            return ("", "")


    def change_hashlib(self, password):
        '''将明文转换成密文'''
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        ret = md5.hexdigest()
        return ret


    def check_user(self, user, name, kind):
        '''校验账号'''
        for k, v in name:
            if 'username' == k and user == v.split('：')[-1].strip():
                passwd = self.change_hashlib(input('请输入密码 :').strip())
                if passwd == name.__next__()[-1].split('：')[-1].strip():
                    return user, passwd, name.__next__()[-1], name.__next__()[-1], name.__next__()[-1], kind
                else:
                    print('密码校验失败！')
                    return False


    def login(self):
        '''登录验证'''
        for i in range(3):  # 3次机会
            user = input('请输入登录名 :').strip()
            if user in ss.admin_dict:  # 优先校验管理员账号，管理员账号总会比普通账号少嘛。
                passwd = self.change_hashlib(input('请输入管理员密码 :').strip())
                if ss.admin_dict[user] == passwd:
                    print("*" * 25 + '\n登录成功！%s管理员！' % user)
                    return user
                else:
                    print('管理员密码校验失败！')
                    continue
            # 讲师账号校验
            teacher = Certification().read_information(ss.teacher_file)  # 读取讲师账号信息文件，返回迭代器
            ret = self.check_user(user, teacher, 'teacher')
            if ret:
                print("*" * 25 + '\n登录成功！%s讲师！' % user)
                return ret
            # 学生账号校验
            student = Certification().read_information(ss.student_file)  # 读取学生账号信息文件，返回迭代器
            ret = self.check_user(user, student, 'student')
            if ret:
                print("*" * 25 + '\n登录成功！%s同学！' % user)
                return ret
            else:
                print('账号不存在！')
        else:
            print('您的3次尝试机会已用完，谢谢使用！')
            return False


if __name__ == '__main__':
    Certification().login()
