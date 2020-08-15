#!usr/bin/python3
import os_chmod,sys

# 首页到目录 '/Users/guojialin/PycharmProjects/shell_'
os_chmod.chdir('shell_')

# 输出到当前目录
print('current dir is %s' % os_chmod.getcwd())

# 打开新目录 '/tmp'
fd = os_chmod.open('/tmp', os_chmod.O_RDONLY)

# 使用 os.fchdir() 方法修改到新目录
os_chmod.fchdir(fd)

# 输出当前目录
print('current dir is %s' % os_chmod.getcwd())

# close current dir
os_chmod.close(fd)
