#!usr/bin/python3
import sys,os,stat

# 打开文件
fd = os.open('foo.txt',os.O_RDONLY)

# 设置文件的用户 id 为 100
os.fchown(fd,100,-1)

print('modify success ')
os.close(fd)

