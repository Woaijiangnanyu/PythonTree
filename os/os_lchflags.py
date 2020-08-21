#!usr/bin/python3
import os,stat

# 打开文件
path = (os.getcwd() + '/lchflags.txt').encode()
fd = os.open(path,os.O_RDWR|os.O_CREAT)

# 关闭文件
os.close(fd)

# 修改标记文件
os.lchflags(path,stat.UF_IMMUTABLE)

# 修改标记成功
print('修改标记成功')