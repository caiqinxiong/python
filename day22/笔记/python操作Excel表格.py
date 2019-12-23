'''
pip install xlrd

# 学习参考:
    -- https://www.cnblogs.com/Neeo/articles/11650149.html
'''

import xlrd

book = xlrd.open_workbook(r'D:\python自动化27day22\测试用例数据.xlsx')
sheet = book.sheet_by_index(0)  # 按照sheet所在的索引位置,从0开始
# book.sheet_by_name('Sheet1')  # 按照sheet名字
# print(sheet.ncols)
# print(sheet.nrows)
#

# 读取所有行
# for row in range(0, sheet.nrows):
#     print(sheet.row_values(row))


# 读取所有列
# for col in range(0, sheet.ncols):
#     print(sheet.col_values(col))

# 将表格的title和下面的每行组成一个字典

'''
    [
        {"case_url": 'https://cnodejs.org/api/v1/topics', "case_method": "get"}
        {"case_url": 'https://cnodejs.org/api/v1/topics', "case_method": "get"}
    ]
'''


# title
# title = sheet.row_values(0)
# # print(title)
# l = []
# for row in range(1, sheet.nrows):
#     l.append(dict(zip(title, sheet.row_values(row))))
# print(l)








