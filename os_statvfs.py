#!usr/bin/python3
import os

# 显示'os_link.py' 文件的statvfs信息
# 返回值
# 返回的结构:
# f_bsize: 文件系统块大小
# f_frsize: 分栈大小
# f_blocks: 文件系统数据块总数
# f_bfree: 可用块数
# f_bavail:非超级用户可获取的块数
# f_files: 文件结点总数
# f_ffree: 可用文件结点数
# f_favail: 非超级用户的可用文件结点数
# f_fsid: 文件系统标识 ID
# f_flag: 挂载标记
# f_namemax: 最大文件长度

stinfo = os.statvfs('os_link.py')

print(stinfo)
