x=99
def f1():
    print(x)
    x=88
def f2():
    x=88
    print(x)

try:
    f1()
except Exception as e:
    print(e)

f2()

print('=================')
def f(x=[]):
    x.append(1)
    print(x)
f()
f()
f()
def f(x=None):
    if x==None:
        x=[]
    print(x)
f()
f()
f()