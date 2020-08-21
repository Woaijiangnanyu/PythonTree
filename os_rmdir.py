#!usr/bin/python3
import os

# 列出目录
print('目录为：%s'%os.listdir(os.getcwd()))

# 要删除的路径
os.rmdir('daily')

# 列出目录
print('目录为：%s'%os.listdir(os.getcwd()))