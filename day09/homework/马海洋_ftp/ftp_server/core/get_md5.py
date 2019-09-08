#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/6'

import hashlib

class Get_md5:
    '''获取md5值'''

    @staticmethod
    def get_md5(user,pwd):
        '''
        用户密码信息加密加盐
        :param user: 登陆用户
        :param pwd:  登陆密码
        :return: 返回加密字符串
        '''
        # 实例化对象，并且加盐
        md5 = hashlib.md5('{0}的梦想是去全世界各种地方逛逛'.format(user).encode('utf8'))
        md5.update(pwd.encode('utf8')) # 更新密码
        return md5.hexdigest()

    @staticmethod
    def file_get_md5(file):
        '''
        获取文件MD5
        :param file: 文件路径
        :return: 文件MD5
        '''
        md5 = hashlib.md5()
        with open(file, mode='rb') as fp:
            for line in fp:
                md5.update(line)
        return md5.hexdigest()


