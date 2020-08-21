#!usr/bin/python3
import os,sys

path = 'foo.txt'

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print('Major 设备号：',major_dnum)
print('Minor 设备号：',minor_dnum)

# 生成设备号
dev_num = os.makedev(major_dnum,minor_dnum)
print('设备号：',dev_num)
