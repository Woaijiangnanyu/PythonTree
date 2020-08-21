#!usr/bin/python3
import sys,os

# 列出目录
print('目录名称：%s'%os.listdir(os.getcwd()))

# 移除
os.remove('lseek.txt')

# 移除后列出目录

print('移除后目录名称 %s'%os.listdir(os.getcwd()))
