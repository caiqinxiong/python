一、环境准备
    说明：之前已安装配置过Python，所以只需要安装一下两个模块即可

    1、安装条形码模块python-barcode
        执行命令： pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-barcode

    2、安装Word文档操作模块python-docx
        执行命令： pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-docx

二、程序操作说明
    1、源数据导入
    将需要生成条形码的信息在db/input目录下的content.txt文件中填写。
    注意：填写完成content.txt文件后关闭，确保文件没有被占用，避免读取失败。

    2、执行程序
    进入bin目录下，双击run.bat脚本

    3、数据生成
    生成的条形码文档在db下的output目录里，带有当前执行时间戳


三、其他说明：
1、配置文件修改
  所有基本配置在conf目录下的settings.py里，可以根据自己需求配置。

2、请勿删除或修改img目录下的图片以及input目录下的content.txt的名称
   （真想改的话需要同步在settings文件里同步修改）

