'''
可以用线程池Pool的方式批量创建子进程
'''
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %.2f seconds'%(name,(end-start)))
if __name__=='__main__':
    print('Parent process %s'%os.getpid())
    p=Pool(4)                                       #这里创建一个Pool，可以同时处理4个进程，但Pool中的进程数量未定
    for i in range(7):                              #为Pool添加7个进程
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()                                       #在join前调用close结束批进程定义
    p.join()                                        #开始同步运行Pool中的进程
    print('All subprocesses done...')