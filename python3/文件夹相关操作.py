#coding:utf-8

import os

# 创建文件夹
os.scandir()
if not os.path.exists('dir2'):      # 判断是否存在dir 不存在就创建
    os.mkdir('dir2')
# 获取当前目录
p = os.getcwd()
print(p)
# 改变默认目录
os.chdir('../')
p = os.getcwd()
print(p)
# 获取目录列表
list = os.listdir('./')
print(list)
# 删除文件夹
os.rmdir('python3/dir2')
