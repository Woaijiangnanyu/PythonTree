#!usr/bin/python3
import os,sys

# 切换到 "/var/www/html" 目录
os.chdir('/var/www/html')

# 打印当前目录
print('打印当前目录： %s' %os.getcwd())

# 打开 /tmp 目录
fd = os.open('/tmp',os.O_RDONLY)

# 使用 os.fchdir() 修改目录
os.fchdir(fd)

# 打印当前目录
print('获取当前目录：' %os.getcwd())

# 关闭文件
os.close(fd)

# 关闭文件成功
print('关闭文件成功')



