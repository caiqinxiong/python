#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/4'

import os
import sys
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from core.main import main

if __name__ == '__main__':
    # 程序入口
    main()
