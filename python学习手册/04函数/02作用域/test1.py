print('==========工厂函数')
def maker1(n):
    def action(x):
        return x*n
    return action
f=maker1(3)
print(f(3))

def maker2():
    x=88
    def action(x=x):
        print(x)
    return action
f=maker2()
f()

def maker3():
    x=99
    return lambda x=x:x
f=maker3()
print(f())

print('############### maker4')
x = 'topx'
def maker4():
    x = 'maker4x'
    def f1():
        y = 'f1x'
        def f2():
            nonlocal x
            print(x)
            # global x
            # print(x)
            # import test1
            # x=test1.x = 'update from modules'
            # print(x)
            # import sys
            # glob = sys.modules['test1.py']
            # x = glob.x
            # print(x)
        f2()
    f1()
maker4()

import builtins
print(dir(builtins))

