#!usr/bin/python3
import os,sys
print('The child will write text to a pipe and ')
print('the parent will read the text written by child')

# 文件描述符 r,w 用于读、写
r,w = os.pipe()

# 使用fork创建子进程后，子进程会复制父进程的数据信息，而后程序就分为两个进程继续运行后面的程序，这也是fork（分叉）名字的含义，在子进程内，这个方法会返回0；
# 在父进程内，这个方法会返回子进程的编号PID
processid = os.fork()

if processid:
    # 父进程
    # 关闭文件描述符 w
    os.close(w)
    r = os.fdopen(r)
    print('Parent reading')
    str = r.read()
    print('text = ',str)
    sys.exit(0)

else:
    # 子进程
    os.close(r)
    w = os.fdopen(w,'w')
    print('child writting ')
    w.write("text written by child ...")
    w.close()
    print('Child closing')
    sys.exit(0)
