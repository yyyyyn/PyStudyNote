'''
找出单个目录下最大的Python源代码文件
搜索windows Python源代码库，除非指定了dir命令行参数
'''
import os,glob,sys

dirname=r'C:\Users\User\Desktop\py_work' if len(sys.argv)==1 else sys.argv[1]

allsizes=[]
allpy=glob.glob(dirname+os.sep+'*.py')
for f in allpy:
    filesize=os.path.getsize(f)
    allsizes.append((filesize,f))
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])