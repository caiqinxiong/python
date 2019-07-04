# -*- coding:utf-8 -*-
# Author:caiqinxiong
# https://www.cnblogs.com/alex3714/articles/5161349.html

import shutil #文件／文件夹高级处理，压缩
import zipfile

# f1 = open('goods_list.txt',encoding="utf-8")
# f2 = open('copyFile.txt','w',encoding="utf-8")
# shutil.copyfileobj(f1,f2) #复制文件内容

# shutil.copyfile('copyFile.txt','copyFile2.txt') #不需要open了，直接就可以复制
# shutil.copy('copyFile.txt','copyFile2.txt') #文件和权限都拷贝了
# shutil.copy2('copyFile.txt','copyFile2.txt') # 拷贝文件和状态信息
# shutil.copytree(src,dst) # 递归都拷贝文件,目录递归复制
# shutil.rmtree(dir) #递归删除目录，不提示
# shutil.move(dir) #递归移动目录，不提示
# shutil.make_archive("aaa",'zip',root_dir='../day04') #将day04在当前目录下压缩成aaa.zip

#单独压缩一个或多个文件
'''
z=zipfile.ZipFile('bbb.zip','w')
z.write('copyFile.txt')
print("中间可以执行其他语句")
z.write('copyFile2.txt')
z.close()
'''