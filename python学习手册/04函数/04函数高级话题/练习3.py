'''
模块计时
'''

import time
reps=1000
repslist=range(reps)

def timer(func,*pargs,**kargs):
    start=time.clock()
    for i in repslist:
        ret=func(*pargs,**kargs)
    elapaed=time.clock()-start
    return (elapaed,ret)

def f():
    return 'hello'

print(timer(f))