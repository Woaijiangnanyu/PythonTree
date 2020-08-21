#!usr/bin/python3
import os,sys

# 显示当前目录
print('当前目录：%s'%os.getcwd())

# 修改当前目录到 /copy/link.txt
fd = os.open(os.getcwd()+'/copy/link.txt',os.O_RDONLY)

f = os.tcgetpgrp(fd)

print('相关进程：')
print(f)

# 关闭文件
os.close(fd)

print('关闭文件成功')

# OSError: [Errno 25] Inappropriate ioctl for device