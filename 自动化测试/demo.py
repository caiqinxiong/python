# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/15 上午9:54

import requests

# response = requests.get(url='http://www.baidu.com')
# print(response)
# print(response.status_code)
# print(response.url)
# print(response.encoding) # 百度的默认编码ISO-8859-1
# print(response.cookies)
# response.encoding = 'utf-8' # 转换一下编码
# # print(response.text) # 文本类型
# # print(response.content) # 二进制
# print(response.headers)

response = requests.request(method='get',url='http://www.baidu.com',timeout=5)
print(response)