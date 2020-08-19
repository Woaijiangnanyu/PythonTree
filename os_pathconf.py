#!usr/bin/python3
import os,sys

# 打开文件
fd = os.open('pathconf.txt',os.O_RDWR | os.O_CREAT)

print('%s'%os.pathconf_names)

# 获取文件最大连接数
no = os.fpathconf(fd,'PC_LINK_MAX')
print('Maximum number of links to the file. :%d'%no)

# 获取文件名最大长度
len = os.fpathconf(fd,"PC_NAME_MAX")
print('Maximum length of a fileName :%d'%len)

# 关闭文件
os.close(fd)

print('关闭文件成功')
