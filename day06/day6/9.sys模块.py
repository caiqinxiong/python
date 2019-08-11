# sys模块
import requests
import sys
import time
# print(time.time())
# print(sys.modules['time'].time())
# print(time == sys.modules['time'])
# sys.modules描述的是当前执行代码位置,解释器中导入的所有模块都会被放到字典里
# 字典的key就是模块的名字,对应的value是这个模块对应的在内存中位置

# import requests
# content = requests.get('http://www.baidu.com')
# print(content.content)
# print(sys.path)
# 1.能不能导入一个模块就要看这个模块所在的路径在不在sys.path中
# 2.如果在sys.path中寻找数据的时候,能够找到一个文件,那么就不继续往下走了
# 3.pycharm会自动的把当前的项目路径添加到sys.path中来,在实际的生产环境中不应该出现这个值

# sys.argv 在执行当前文件的时候传递一些参数到python代码中来
# print(sys.argv)
# if sys.argv[1] == 'alex' and sys.argv[2] == '3714':
#     print('登录成功,可以执行接下来的脚本功能')
# else:
#     print('错误的用户名和密码')
#     exit()
#
# print('欢迎你使用xxx公司的自动化部署脚本')