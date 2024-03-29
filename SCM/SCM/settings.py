"""
Django settings for SCM project.

Generated by 'django-admin startproject' using Django 1.11.25.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cz_t5bph@@(gnq07itt#w!@o9ew4@q&4cbpeltig8ud+!4m)0='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',  # 验证码
    'rim.apps.RimConfig',  # 自定义项目APP
    'xadmin',  # xamin主体模块
    'crispy_forms',  # 渲染表格模块
    'reversion',  # 为模型通过版本控制，可以回滚数据

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rim.middlewares.authmid.AuthMD',
]

ROOT_URLCONF = 'SCM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SCM.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 验证码设置：django_simple_captcha 验证码配置其他配置项查看文档
# 默认格式
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_NOISE_FUNCTIONS = (  # 'captcha.helpers.noise_null', # 没有样式
    'captcha.helpers.noise_arcs',  # 线
    'captcha.helpers.noise_dots',  # 点
)
# 图片中的文字为随机英文字母，如 mdsh
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为数字表达式，如2+2=
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 超时(minutes)
CAPTCHA_TIMEOUT = 1
# 验证码宽度和高度
# CAPTCHA_IMAGE_SIZE = (100, 25)

# session 设置
# SESSION_COOKIE_NAME ＝ "sessionid"       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"               # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）（数字为秒数）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）

# 邮箱设置
# EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST = 'smtp.qq.com'
# 设置端口号，为数字
# EMAIL_PORT = 25
EMAIL_PORT = 587
# 设置发件人邮箱
EMAIL_HOST_USER = 'xxx@qq.com'
DEFAULT_FROM_EMAIL = 'xxx@qq.com'
# 设置发件人 授权码不是密码
EMAIL_HOST_PASSWORD = 'xxx'
# 设置是否启用安全链接
EMAIL_USER_TLS = True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
# 以上这个配置信息，Django会自动读取，
# 使用账号以及授权码进行登录，
# 如果登录成功，可以发送邮件


# 过滤自动获取的路由
AUTO_DISCOVER_EXCLUDE = [
    '/admin/.*',
    '/xadmin/.*',
    '/rim/login/',
    '/rim/logout/',
    '/index/',
    '/captcha'
]

# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/media/')

try:
    from .local_settings import *
except ImportError as e:
    print(e)