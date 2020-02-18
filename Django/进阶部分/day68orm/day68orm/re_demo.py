"""
这是给S10 孟宾（mengbi） 同学讲re的分组
"""

import re

r = re.compile(r'^delete/([a-zA-Z]+)/(\d+)/$')

ret = r.match("delete/author/10/")
print(ret.groups())
print(ret.group(1))
print(ret.group(2))
