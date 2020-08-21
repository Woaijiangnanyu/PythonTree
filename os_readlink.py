#!usr/bin/python3
import os

src = os.getcwd() + '/copy/link.txt'
dst = os.getcwd() + '/dmplink'

# 创建软连接
os.symlink(src,dst)

# 使用软连接显示原链接
path = os.readlink(dst)
print(path)

