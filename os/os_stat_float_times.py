#!usr/bin/python3
import os

# stat 信息
statinfo = os.stat('os_link.py')

print(statinfo)

# 参数
# newvalue -- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。
statinfo = os.stat_float_times()

print(statinfo)

# 3.7 弃用
# AttributeError: module 'os' has no attribute 'stat_float_times'