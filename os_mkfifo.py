#!usr/bin/python3
import os,sys

# 创建目录
path = os.getcwd() + '/hourly'
os.mkfifo(path,0o644)

print('路径被创建')