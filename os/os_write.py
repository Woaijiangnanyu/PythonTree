#!usr/bin/python3
import os

# 打开文件
fd = os.open('write.txt',os.O_RDWR | os.O_CREAT)

# 写入字符串
str = 'This is runoob.txt'.encode('UTF-8')
ret = os.write(fd,str)

# 输出返回值
print('写入的位数为：')
print(ret)
print('写入成功')

# 关闭文件
os.close(fd)

print('关闭文件成功')
