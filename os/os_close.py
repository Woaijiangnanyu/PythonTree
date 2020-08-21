#!/usr/bin/python3
from os import os_dup2

# 打开文件
fd = os_dup2.open('foo.txt', os_dup2.O_RDWR | os_dup2.O_CREAT)

# 写入字符串
os_dup2.write(fd, "This is test".encode())

# 关闭文件
os_dup2.closerange(fd, fd)

print('close file success')
