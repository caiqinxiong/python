# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/29 14:36
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import main

if __name__ == '__main__':
    main.main()