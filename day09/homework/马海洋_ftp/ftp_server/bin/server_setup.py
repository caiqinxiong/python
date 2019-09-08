#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/3'

# 初始化项目库
import os
import sys
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

# 导入主函数
from core.main import main

# 程序入口
if __name__ == '__main__':
    main()

