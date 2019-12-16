# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/4 14:16

import datetime
d1 = datetime.datetime.strptime('2019/11/20 15:19:50', '%Y/%m/%d %H:%M:%S')
d2 = datetime.datetime.strptime('2015/03/02 17:41:20', '%Y/%m/%d %H:%M:%S')
print(d1)
print(d2)
delta = d1 - d2
print(delta)
print(delta.days)
print(delta.seconds)

