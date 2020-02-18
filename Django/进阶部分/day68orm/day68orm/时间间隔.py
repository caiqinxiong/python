"""
时间间隔
"""

import datetime


now = datetime.datetime.now()  # 你领了一张有效期为7天的优惠券
print(now)
# 时间间隔
d7 = datetime.timedelta(weeks=52)
# 求失效时间
ret = now + d7
print(ret)
