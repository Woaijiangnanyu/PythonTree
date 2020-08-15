#!usr/bin/python3
import sys,os

# 打开文件
fd = os.open('ftruncate.txt',os.O_RDWR|os.O_CREAT)

# 写入文件
os.write(fd,'this is test - this is test'.encode())

# 使用ftruncate() 方法
os.ftruncate(fd,10)

# 读取内容
os.lseek(fd,0,0)
str = os.read(fd,100)

# 打印字符
print('字符串 ： ',str)

# 关闭文件
os.close(fd)

# 关闭成功
print('关闭成功')

