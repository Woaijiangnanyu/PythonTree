#!usr/bin/python3
import os,sys

# 打开文件
fd = os.open('lseek.txt',os.O_RDWR|os.O_CREAT)

# 写入数据
os.write(fd,'this my test file'.encode())

# 强行写入
os.fsync(fd)

# 从头开始读取
os.lseek(fd,0,0)
str = os.read(fd,100)

print('读取文件：',str)

# 关闭文件
os.close(fd)

# 关闭文件成功
print('关闭文件成功')

