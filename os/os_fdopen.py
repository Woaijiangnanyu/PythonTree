#!usr/bin/python3
import sys,os

# 打开文件
fd = os.open('foo.txt',os.O_RDWR | os.O_CREAT)

# 通过文件描述符创建一个文件对象
fo = os.fdopen(fd,'w+')

# 获取当前位置
print('current I/O pointer position :%d' %fo.tell())

# 写入字符串
fo.write('Python is a great language . \n Yeah its great !\n')

# 读取内容
# os.lseek() 方法用于设置文件描述符fd当前位置为pos,how 方式修改
os.lseek(fd,0,0)
str = os.read(fd,100)

print('read string is: ',str)

# 获取当前位置
print('current I/O pointer position :%d' %fo.tell())

# 关闭文件
os.close(fd)

print("关闭文件成功")