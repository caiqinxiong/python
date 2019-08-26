# import logging
# fh = logging.FileHandler(filename='xxx.log',encoding='utf-8')
# fh1 = logging.FileHandler(filename='xxx2.log',encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(level=logging.INFO,
#                     handlers=[fh,sh,fh1],
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s[%(lineno)d] - %(levelname)s -%(module)s:  %(message)s')
# logging.debug('debug message')      # 情况越轻
# logging.info('info message')        # 信息类的日志
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# logging日志分为5个等级
# 默认只显示warning等级以上的信息
# import time
# import logging
# from logging import handlers
# sh = logging.StreamHandler()
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=512,backupCount=5,encoding='utf-8')
# fh = handlers.TimedRotatingFileHandler(filename='myapp2.log', when='s', interval=5, encoding='utf-8')
# logging.basicConfig(level=logging.INFO,
#                     handlers=[rh,fh,sh],
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s[%(lineno)d] - %(levelname)s -%(module)s:  %(message)s')
# while True:
#     logging.warning('您输入了错误的数字,程序造成了一次异常,已被处理')
#     time.sleep(0.3)

















