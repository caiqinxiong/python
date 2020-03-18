# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/3/18 9:55

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'scm',
#         'HOST': '120.192.70.148',
#         'PORT': 3306,
#         'USER': 'root',
#         'PASSWORD': "mysqlroot"
#     }
# }

# 邮箱设置
# EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST = 'smtp.qq.com'
# 设置端口号，为数字
# EMAIL_PORT = 25
EMAIL_PORT = 587
# 设置发件人邮箱
EMAIL_HOST_USER = 'caiqinxiong_cai@qq.com'
DEFAULT_FROM_EMAIL = 'caiqinxiong_cai@qq.com'
# 设置发件人 授权码不是密码
EMAIL_HOST_PASSWORD = 'ynfinymixhlabfaa'
# 设置是否启用安全链接
EMAIL_USER_TLS = True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
# 以上这个配置信息，Django会自动读取，
# 使用账号以及授权码进行登录，
# 如果登录成功，可以发送邮件