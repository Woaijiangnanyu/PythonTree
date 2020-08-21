from os import os_chmod

# open a file
f = open('dup2','a')

# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件
os_chmod.dup2(f.fileno(), 1)

# close file
f.close()

# print 输出到标准输出流,就是文件描述符1
print('runoob')
print('google')
print('alibaba')
