#!usr/bin/python3
import os,stat
path = 'mknod.txt'
mode = 0o777 | stat.S_IRUSR

# 文件系统结点指定不同模式
os.mknod(path,mode)
# PermissionError: [Errno 1] Operation not permitted  root 权限


