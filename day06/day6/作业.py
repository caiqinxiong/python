# 1.给你一个非空文件夹,要求你删掉这个文件夹
    # 进阶需求,这个非空文件夹下还有其他非空文件夹,并且不知道有多少层
# 2.b以下 对照讲解视频把计算器作业再写一写
    # 50行以内的代码
# 3.sys.argv 和os模块 完成一个大作业
    # 完成文件的copy: 从dir1 到dir2的copy
    # 文件\文件夹的size
    # 移动文件: 从dir1 到dir2
    # 重命名文件/文件夹

# python xxx.py copy F:\python自动化27期\day6 F:\python自动化27期\day5
# python xxx.py size F:\python自动化27期\day6\xxx.txt
# python xxx.py size F:\python自动化27期\day6
# python xxx.py move F:\python自动化27期\day6\xxx.txt F:\python自动化27期\day5\xxx.txt
# python xxx.py rename F:\python自动化27期\day6\xx1.txt F:\python自动化27期\day5\xx2.txt

# 求size 我们中午的时候做了
# rename 直接用现成的os.rename
# copy和move
    # 打开第一个路径 读的方式  打开第二个路径写的方式

# os模块的熟悉
# sys.argv
# 函数的封装