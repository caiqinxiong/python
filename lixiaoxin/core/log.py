# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/3 16:03
import logging
import sys
import time
from logging import handlers
from conf import settings as ss

class Log(object):
    '''
    https://cloud.tencent.com/developer/article/1354396
    '''
    sh = logging.StreamHandler()  # 既打印输入又写入文件
    # rh = handlers.RotatingFileHandler(ss.log_file, maxBytes=1024,backupCount=5) # 按大小切换日志，保留5份
    fh = handlers.TimedRotatingFileHandler(filename=ss.LOG_FILE, when='D', backupCount=5, interval=5,encoding='utf-8')  # 按时间切割日志
    logging.basicConfig(level=logging.WARNING,  # 打印日志级别
                        handlers=[fh, sh],
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s')  # [%(lineno)d] 只显示当前文件的行号

    @staticmethod
    def writeOnly(content):
        '''自定义函数，只写入日志文件'''
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        with open(ss.LOG_FILE, mode='a', encoding='utf-8') as f:
            f.write(now_time + '\t' + str(content) + '\n')

    @staticmethod
    def readOnly(content):
        '''自定义函数，只打印日志'''
        # print('\033[36;1m%s\033[0m' % content)
        print(content)

    @classmethod
    def readAndWrite(cls,content):
        '''自定义函数，既打印信息又记录log文件'''
        cls.readOnly(content)
        cls.writeOnly('[INFO]\t' + content)

    @classmethod
    def debug(cls, content):
        # return logging.debug(content)
        return cls.readOnly(content)

    @classmethod
    def info(cls, content):
        # return logging.info(content)
        return cls.writeOnly('[INFO]\t' + content)  # info信息直接写入log文件

    @staticmethod
    def warning(content):
        return logging.warning(content)

    @staticmethod
    def error(content):
        # 获取调用函数的文件名和行数
        head = '%s line%s error!\n' % (sys._getframe().f_back.f_code.co_filename, sys._getframe().f_back.f_lineno)
        return logging.error(head + content)

    @staticmethod
    def critical(content):
        head = '%s line%s critical!\n' % (sys._getframe().f_back.f_code.co_filename, sys._getframe().f_back.f_lineno)
        return logging.critical(head + content)
