#!usr/bin/python3
import os,sys

# 打开文件
path = os.getcwd()
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
