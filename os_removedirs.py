#!usr/bin/python3
import os_rename

# 列出目录
print('目录结构：%s' % os_rename.listdir(os_rename.getcwd()))

# 删除目录
os_rename.removedirs('tempdirs')

# 列出删除后的结果
print('目录结构：%s' % os_rename.listdir(os_rename.getcwd()))

