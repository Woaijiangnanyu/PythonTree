#!usr/bin/python3
import os,sys

# 创建目录
path = os.getcwd() + '/daily'
os.makedirs(path,0o755)
print('路径创建成功')
