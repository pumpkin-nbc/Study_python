import random
secret = random.randint(1,10)

import os
os.getcwd()#当前工作目录
os.chdir()#更改工作目录 需要输入字符串
os.listdir()#反馈*下的文件名 需要输入字符串
os.mkdir()#创建单个文件夹 需要输入字符串
os.makedirs()#创建多层文件夹 需要输入字符串
os.remove()#删除文件
os.rmdir()#删除单个目录，必须保证目录内为空
os.removedirs()#删除多个目录。必须保证目录为空
os.rename()#旧名字，新名字  将旧名字修改成新名字
os.system()#运行系统的shell命令
os.curdir #当前目录 .
os.pardir #上一级目录 ..
os.sep#输出操作系统特定的路径分隔符
os.name#输出当前使用的操作系统

os.path.basename()#去除路径反馈文件名'e:\\s\s\sxx.txt' teturm sxx.txt
os.path.dirname()#去除文件名反馈路径
os.path.join()#path1,path2, , , 将path1和path2合成一个路径
os.path.split()#path 分割路径与文件名
os.path.splitext()#分离路径，扩展名
os.path.getsize()#返回指定文件大小
os.path.getatime()#返回访问时间,浮点型秒数 使用gmtime(os.path.getatime())或者localtime(os.path.getatime())转换
os.path.getctime()#返回创建时间,浮点型秒数 使用gmtime(os.path.getctime())或者localtime(os.path.cetatime())转换
os.path.getmtime()#返回修改时间,浮点型秒数 使用gmtime(os.path.getmtime())或者localtime(os.path.getmtime())转换

os.path.exists()#判断指定路径或文件是否存在
os.path.isabs()#判断指定路径是否为绝对路径
os.path.isdir()#判断路径是否存在
os.path.isfile()#判断文件是否存在
os.path.islink()#判断符号链接(快捷方式）是否存在
os.path.ismount()#判断挂载点(盘符）是否存在
os.path.samefile()#path1,path2 判断两个路径是否指向同一个文件