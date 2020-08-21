#!/usr/bin/python3
import os,stat,sys

# 打开文件
fd = os.open('foo.txt',os.O_RDONLY)

# 设置文件可以通过组执行
os.fchmod(fd,stat.S_IXGRP)

# 设置文件可以被其他用户写入
os.fchmod(fd,stat.S_IWOTH)

print('modify success')

# 关闭文件
os.close(fd)

