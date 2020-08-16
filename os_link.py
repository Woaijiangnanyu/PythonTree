#!usr/bin/python3
import os,sys

# 打开文件
path = 'link.txt'.encode()
fd = os.open(path,os.O_CREAT | os.O_RDWR)

# 关闭文件
os.close(fd)

# 创建link链接
dst = 'copy/link.txt'
os.link(path,dst)

# 创建链接成功
print('创建链接成功')
