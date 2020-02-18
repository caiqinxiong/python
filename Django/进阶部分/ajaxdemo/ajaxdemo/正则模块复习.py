"""
Python re校验手机号
"""
import re

r = re.compile(r'^1[3-9][0-9]{9}$')
print(r.match("12211111111"))
print(r.match("13211111111"))
print(r.match("1a211111111"))