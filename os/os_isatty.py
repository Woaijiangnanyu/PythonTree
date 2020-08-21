#!usr/bin/python3

import os,sys

# 打开文件
fd = os.open('isatty.txt',os.O_RDWR | os.O_CREAT)

# 写入文件
str = 'input thes word to file '
os.write(fd,bytes(str,'UTF-8'))

# 使用 isatty () 查看是否存在链接
ret = os.isatty(fd)
print('返回值：',ret)

# 关闭文件
os.close(fd)