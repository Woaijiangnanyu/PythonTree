#!usr/bin/python3
import os,sys
fd = os.open('/Users/guojialin/PycharmProjects/shell_/foo.txt',os.O_RDWR|os.O_CREAT)

# write char to file
os.write(fd,'today is 2020.08.13'.encode())

# input hard disk
os.fdatasync(fd)

# read file
os.lseek(fd,0,0)
str = os.read(fd,100)
print('read char is ： ' ,str)

# close file
os.close(fd)

print('close file success ')

# AttributeError: module 'os' has no attribute 'fdatasync'