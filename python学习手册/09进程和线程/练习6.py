'''
锁：预防多线程操作时数据错乱

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
'''
import threading
balance=0
lock=threading.Lock()       #实例锁对象
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(1000000):
        lock.acquire()      #申请锁，以下的代码一次只能一个线程执行
        try:
            change_it(n)
        finally:
            lock.release()  #结束后要手动释放锁

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)