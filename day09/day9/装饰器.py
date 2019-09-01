# def classmethod(func):
#     def inner(*args,**kwargs):
#         func('类')
#     return inner
#
# def staticmethod(func):
#     def inner(*args,**kwargs):
#         func()
#     return inner
#
# @staticmethod
# def wahaha():
#     print('in 娃哈哈')
#
# @classmethod
# def qqxing(cls):
#     print('in qqxing',cls)
#
# wahaha()
# qqxing()

import sys
def processBar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

processBar(100246000,112132327)