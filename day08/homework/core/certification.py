# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 10:37
import pickle

from conf import settings as ss


class Certification(object):
    '''登录认证类'''

    def __init__(self):
        pass

    def written_information(self, file_name, content):
        '''写入信息'''
        with open('%s' % file_name, mode='ab') as f:
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
                    except EOFError:break
        except:return ("", "")


    def login(self):
        '''登录验证'''
        for i in range(3):  # 3次机会
            user = input('请输入登录名 :').strip()
            if user in ss.admin_dict:  # 优先校验管理员账号，管理员账号总会比普通账号少嘛。
                passwd = input('请输入管理员密码 :').strip()
                if ss.admin_dict[user] == passwd:
                    print("*" * 25 + '\n登录成功！%s管理员！' % user)
                    return user
                else:
                    print('管理员密码校验失败！')
                    continue
            ret = Certification().read_information(ss.student_file)  # 读取学生账号信息文件，返回迭代器
            for k, v in ret:
                if 'username' == k and user == v.split('：')[-1].strip():
                    passwd = input('请输入密码 :').strip()
                    if passwd == ret.__next__()[-1].split('：')[-1].strip():
                        print("*" * 25 + '\n登录成功！%s同学！' % user)
                        return user, passwd, ret.__next__()[-1], ret.__next__()[-1], ret.__next__()[-1]
                    else:
                        print('密码校验失败！')
            else:
                print('账号不存在！')
        else:
            print('您的3次尝试机会已用完，谢谢使用！')
            return False

if __name__ == '__main__':
    Certification().login()
