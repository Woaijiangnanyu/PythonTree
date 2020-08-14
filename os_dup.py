#!/usr/bin/python3
import os_dup2,sys

# 打开文件
fd = os_dup2.open('foo.txt', os_dup2.O_RDWR | os_dup2.O_CREAT)

# 复制文件描述符
d_fd = os_dup2.dup(fd)

# 使用复制文件描述写入文件
os_dup2.write(d_fd, 'This is test - '.encode())

# 关闭文件
os_dup2.closerange(fd, d_fd)

print('close file is success ！')