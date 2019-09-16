'''
同时实现多任务的方式：
多进程模式；
多线程模式；
多进程+多线程模式。

getpid():得到当前进程id
getppid()：得到父进程id
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''

import os
from multiprocessing import Process
'''
#函数fork()在linux和mac上可以，在windows上不可以，windows上要实现多线程可以用multiprocessing模块
pid=os.fork()
if pid==0:
    print('I am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s)'%(os.getppid(),pid))
'''

def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getppid()))

if __name__=='__main__':
    print('Parent process %s'%os.getpid())       #获取当前进程id
    p1=Process(target=run_proc,args=('test1',))    #创建进程实例
    p2=Process(target=run_proc, args=('test2',))
    print('Child process will start')
    p1.start()                                    #启动进程
    p2.start()
    p1.join()
    p2.join()
    print('Child process end')                     #只有当上面join的子线程结束时才会运行接下来的主体程序