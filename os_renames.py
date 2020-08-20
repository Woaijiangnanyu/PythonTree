#!usr/bin/python3
import os

# 当前目录
print(os.getcwd())

# 当前目录结构
print(os.listdir(os.getcwd()))

# 改变文件名称
os.renames('foo.txt','nwdirs/Foo.txt')

# 改变目录成功
print('改变目录成功')

# 当前目录结构
print(os.listdir(os.getcwd()))