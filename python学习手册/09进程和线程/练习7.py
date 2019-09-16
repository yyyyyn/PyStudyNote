'''
线程调用的是相同的函数，不方便为单个线程指定特定的变量
可以使用local全局变量使线程使用自己独特的局部变量，互不干扰
'''
import threading

local_school = threading.local()        # 创建全局ThreadLocal对象:

def process_thread(name):
    local_school.student = name         # 绑定ThreadLocal的student:
    process_student()

def process_student():
    std = local_school.student          # 获取当前线程关联的student:
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()