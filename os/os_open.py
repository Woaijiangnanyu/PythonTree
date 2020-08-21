#!usr/bin/python3
import sys,os

# 打开文件
fd = os.open('open.txt',os.O_RDWR | os.O_CREAT)

# 写入文件
os.write(fd,"this is a test ...".encode())

# 关闭文件
os.close(fd)

print('关闭文件')