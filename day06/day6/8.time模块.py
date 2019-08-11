# 什么时候需要时间
# 打印日志
# 计算效率 : keep
# 登录
# 注册的时间
# 下单时间

# time
import time
# 时间戳时间
# print(time.time())

# 结构化时间 tm_isdst:夏令时
# ret = time.localtime()
# print(ret)

# 格式化时间 time模块的格式化不支持中文
# ret= time.strftime('%Y-%m-%d %H:%M:%S')
# ret= time.strftime('%c')
# print(ret)

# stime = '2018-08-08 11:08:08'
# struct_t = time.strptime(stime,'%Y-%m-%d %H:%M:%S')
# print(struct_t)
# stamp_time = time.mktime(struct_t)
# print(stamp_time)  # 1533697688

# stamp = 3000000000
# struct_t = time.localtime(stamp)
# print(struct_t)
# fmt_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_t)
# print(fmt_time)

# datetime
from datetime import datetime
# dt = datetime.now()
# print(dt.day)
# print(dt.month)
# print(dt.year)
# print(dt.hour)

# from datetime import timedelta
# print(dir(timedelta))
# dt1 = datetime(2019, 8, 11, 17, 8)
# dt2 = datetime(2019, 8, 12, 19, 3)
# res = dt2 - dt1
# print(res,type(timedelta))
# print(res.days)     # 差了多少天
# print(res.seconds)  # 差了除了天之外的多少秒
# print(res.total_seconds())  # 包括天在内的多少秒
# print(res.total_seconds()//3600)

# s1 = '2017/9/30'
# s2 = '2017年9月30日Saturday'
# s3 = '2017年9月30日星期六8时42分24秒'
# s4 = '9/30/2017'
# s5 = '9/30/2017 8:42:50'
# str -->datetime  strptime
# ret = datetime.strptime(s1,'%Y/%m/%d')
# print(ret,type(ret))

# ret = datetime.strptime(s2,'%Y年%m月%d日%A')
# print(ret,type(ret))

# datetime --> str strftime
# dt = datetime(2019, 8, 11, 17, 8,0)
# print(dt)
# ret = dt.strftime('%Y年%m月%d日 %H点%M分')

# from datetime import datetime
# i=datetime(2017,9,28,10,3,43)
# print(i.strftime('%Y-%m-%d %A,%H:%M:%S'))



# time
# 当前月的1号对应的0点的时间戳时间
# import time
# def get_stamp():
#     strt = time.strftime('%Y-%m-01 00:00:00')
#     struct_t = time.strptime(strt,'%Y-%m-%d %H:%M:%S')
#     stamp_t = time.mktime(struct_t)
#     return stamp_t

# time
# t2的时间 t1的时间 t2 - t1 经历了多少年  月  日  时 分 秒
# t1 = '2017-7-11 11:11:11'
# t2 = '2019-9-03 08:43:07'
# # 过去了多少年月日时分秒
# # t1 --> 时间戳时间1
# # t2 --> 时间戳时间2
# # 时间戳时间2 - 时间戳时间1 = 时间戳时间小数
# # 时间戳时间小数 --> 结构化时间
# def time_sub(t1,t2):
#     struct_t1 = time.strptime(t1,'%Y-%m-%d %H:%M:%S')
#     stamp1 = time.mktime(struct_t1)
#     struct_t2 = time.strptime(t2,'%Y-%m-%d %H:%M:%S')
#     stamp2 = time.mktime(struct_t2)
#     res = abs(stamp2 - stamp1)
#     struct_t = time.gmtime(res)
#     return (struct_t.tm_year-1970,struct_t.tm_mon-1,struct_t.tm_mday-1,struct_t.tm_hour,struct_t.tm_min,struct_t.tm_sec)
#
# ret = time_sub(t1,t2)
# print(ret)
