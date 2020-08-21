#!usr/bin/python3

import os

src = os.getcwd() + '/copy/link.txt'
dst = os.getcwd() + '/nwdirs/link.txt'

# 创建软连接
os.symlink(src,dst)

print('创建链接成功')
