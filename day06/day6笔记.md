## re模块

### 常用方法

##### findall(正则表达式,带匹配的字符串)

```python
# 功能 :取所有
# 返回值 :列表,所有匹配到的项都会被返回到列表中
phone_num = input('请输入合法的手机号:')
regex = r'^1[2-9]\d{9}$'
ret = re.findall(regex,phone_num)
print(ret)

# findall和分组的关系
ret = re.findall('\d(\d)','a1,b22,c345')
print(ret)  # [2,4]
# ?:取消分组优先显示
ret = re.findall('\d(?:\d)','a1,b22,c345')
print(ret)  # ['22', '34']
```

##### search(正则表达式,带匹配的字符串)

```python
# 功能:从头开始往后找任何地方有符合条件的都返回一个
# 返回值:re自定义类型
phone_num = input('请输入合法的手机号:')
regex = r'^1[2-9]\d{9}$'
ret = re.search(regex,phone_num)
if ret:
    print('是合法的手机号码 %s'%phone_num)
else:
    print('不是合法的手机号码')

# search取分组中的内容:根据序号取,根据组名取
ret = re.search('(?P<num1>\d)(?P<num2>\d)','a1,b28,c345')
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group('num1'))
print(ret.group('num2'))

# 分组的引用 ?P=num1表示引用了num1分组,匹配到的内容必须和num1分组中的内容一模一样
ret = re.search('(?P<num1>\d)(?P=num1)','a14,b22,c3357')
print(ret.group())
```

##### match(正则表达式,带匹配的字符串) - 匹配用户输入的内容是否合法时候都是用match

```python
# 功能:从头开始匹配,如果开始部分匹配到了就是匹配成功,如果开始部分没匹配到,就匹配失败
# 返回值:re自定义类型
phone_num = input('请输入合法的手机号:')
regex = r'1[2-9]\d{9}$'
ret = re.match(regex,phone_num)
if ret:
    print(ret)
    print('是合法的手机号码 %s'%phone_num)
else:
    print('不是合法的手机号码')
```

### 了解内容

```python
# 根据正则做切割
ret = re.split(r'\d+',r'alex84wusir73')
print(ret)

# sub  替换方法(正则表达式,要替换的内容,待替换的字符串,要替换的个数)
ret = re.sub(r'\d+','H','eva123alex456',1)
print(ret)

# subn 替换方法2 返回值会是一个元组,第一项是结果,第二项是替换次数
ret = re.subn(r'\d+','H','eva123alex456')
print(ret)
```

### 进阶方法

```python
# compile 预编译 预先来编译一下我们写好的正则
rule = re.compile('\d+')
ret = rule.findall('alex123eva456')
print(ret)
ret = rule.findall('手机号码13737373377\n身份证号 110107197712072277')
print(ret)
```

```python
# finditer 返回一个迭代器,循环取出来的是re的自定义类型,通过group取值,能够节省空间
ret = re.finditer('\d','alex1916936916598sb7985073495898632847')
print(ret)
for i in ret:
    print(i.group())
```

## os模块

#### 重点方法

```python
 os.path.getsize(绝对路径) 获取文件的大小,但是不能获取文件夹的准确大小
 os.path.isfile(绝对路径) 判断是否是文件
 os.path.isdir(绝对路径) 判断是否是文件夹
 os.path.join(文件夹的名字,名字) 跨平台的文件路径的拼接
 os.path.split(path) 将path分割成目录和文件名二元组返回 
 os.listdir('文件夹的路径') 显示这个文件夹下的所有名字(包括文件和文件夹)
```

练习 :计算文件夹的大小

```python
递归的方式
import os
def dir_size(path):
    if os.path.isdir(path):
        sumsize = 0
        name_lst = os.listdir(path) # ['move_info7 :2000','dir1','dir2','1.内容回顾.py']
        for name in name_lst:
            full_path = os.path.join(path,name)
            if os.path.isfile(full_path):
                sumsize += os.path.getsize(full_path)  # 2000
            else:                      # dir1
                ret = dir_size(full_path)    # dir_size(F:\python自动化27期\day6\dir1)
                sumsize += ret
        return sumsize
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:print('找不到文件')

path2 = r'F:\python自动化27期\day6'
ret = dir_size(path2)
print(ret)

```

```python
循环的方式
import os
def dir_size(path):
    if os.path.isdir(path):
        sum_size,dirs = 0,[path]
        while dirs:
            path = dirs.pop()
            dir_lst = os.listdir(path)
            for name in dir_lst:
                file_path = os.path.join(path,name)
                if os.path.isfile(file_path):
                    sum_size += os.path.getsize(file_path)
                else:
                    dirs.append(file_path)
        return sum_size
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:
        print('找不到文件')


path2 = r'F:\python自动化27期\day6'
ret = dir_size(path2)
print(ret)
```

#### 其他方法

```python
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息

os.system("bash command")  运行shell命令，直接显示
os.popen("bash command).read()  运行shell命令，获取执行结果
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd

os.path
os.path.abspath(path) 返回path规范化的绝对路径
os.path.split(path) 将path分割成目录和文件名二元组返回 
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 
os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小
```

### time模块

三种时间格式 : 时间戳时间  结构化时间 格式化时间

```python
import time
时间戳 --> 结构化 
结构化时间 = time.localtime(时间戳时间)
结构化 --> 时间戳
时间戳时间 = time.mktime(结构化时间)
格式化时间 -->结构化
结构化时间 = time.strptime(时间,格式)
结构化 --> 格式化时间
格式化时间 = time.strftime(结构化时间,格式)
```

#### datetime模块

```python
from datetime import datetime
创造datetime数据
datetime.now() 获取当前的datetime时间
datetime(2017,8,9,11,22,33)创建一个指定的时间
str类型  --> datetime
datetime时间 = datetime.strptime(字符串,格式)
datetime --> str时间
str时间 = dt.strftime(格式)
```

## sys模块

```python
import sys
# sys.argv 在执行当前文件的时候传递一些参数到python代码中来
print(sys.argv)

# sys.modules描述的是当前执行代码位置,解释器中导入的所有模块都会被放到字典里
# 字典的key就是模块的名字,对应的value是这个模块对应的在内存中位置
print(sys.modules)

sys.path
# print(sys.path)
# 1.能不能导入一个模块就要看这个模块所在的路径在不在sys.path中
# 2.如果在sys.path中寻找数据的时候,能够找到一个文件,那么就不继续往下走了
# 3.pycharm会自动的把当前的项目路径添加到sys.path中来,在实际的生产环境中不应该出现这个值


```

