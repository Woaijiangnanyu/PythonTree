#!usr/bin/python3
import os

# 修改前文件名称
print('修改前目录名称：%s'%os.listdir(os.getcwd()))

# 修改名称
os.rename('Open.txt','open.txt')

# 修改文件名成功
print('修改文件名称成功')

# 修改后的文件名称
print('修改后的文件名称：%s'%os.listdir(os.getcwd()))

