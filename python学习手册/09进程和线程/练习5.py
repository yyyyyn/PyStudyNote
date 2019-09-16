'''
多进程:_thread,threading模块，主要使用后者
启动一个线程就是把一个函数传入并创建Thread实例，然后start()执行

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
'''
import time,threading
def loop():
    print('thread %s is running...'% threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s>>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)

print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended'%threading.current_thread().name)