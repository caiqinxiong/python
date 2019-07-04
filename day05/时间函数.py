# -*- coding:utf-8 -*-
# Author:caiqinxiong
import  time,datetime
#时间戳---元组---格式化时间 （三者之间的转换）
print(time.localtime()) #将时间戳转换为元组，结果为UTC+8时区，传人'秒'参数，不传人默认当前时间
print(time.gmtime(123244342))#将时间戳转换为元组，结果为UTC时区，传人'秒'参数，不传人默认当前时间
print(time.time())#打印时间戳，从1970年到现在一共多少秒
print(time.gmtime(123244342).tm_year) #获取这个时间戳到年份
print(time.gmtime(123244342).tm_hour)  #获取该时间戳到小时
print(time.localtime().tm_hour)
print(time.mktime((1973, 11, 27, 10, 32, 22, 1, 331, 0))) # 将元组（9个参数）的格式转换为时间戳

T=time.localtime(738468244)
print(time.strftime("%Y-%m-%d %H:%M:%S",T)) #格式化输出时间，自定义,将元组转换成格式化
print(time.strptime("1993-05-27 10:04:04","%Y-%m-%d %H:%M:%S")) #将格式化时间转换成元组，后面的格式需要一一对应

print('\n#########################')
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

print('\n#########################')
print(datetime.datetime.now()+datetime.timedelta(hours=-12))#前十二个小时
print(datetime.datetime.now()+datetime.timedelta(hours=12))#十二小时后，时间相加
print(datetime.datetime.now()+datetime.timedelta(minutes=30))#三十分钟后，时间相加
print(datetime.datetime.now()+datetime.timedelta(2))#两天后，当前时间+2天
print('\n#########################')
nowTime=datetime.datetime.now()
print(nowTime)
print(nowTime.replace(hour=10,minute=10))#时间不对，可以替换


