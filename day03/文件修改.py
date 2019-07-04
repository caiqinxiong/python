# -*- coding:utf-8 -*-
# Author:caiqinxiong
import sys
find_str = sys.argv[1]
replace_str = sys.argv[2]
f = open('goods_list.txt','r',encoding='utf-8')
f_new = open('goods_list.txt.bak','w',encoding='utf-8')
for line in f:
    if find_str in line:
        #直接替换
        line=line.replace(find_str,replace_str )
    f_new.write(line)
f.close()
f_new.close()