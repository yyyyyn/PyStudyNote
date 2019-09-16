print('==========函数内省')
def f():
    x='abc'
    return x

print(f.__code__)

print('==========函数注解')
def f(a:'spam',b,c:99)->int:
    return a+b+c
print(f.__annotations__)
print(f(1,2,3))

print('==========lambda')
def f():
    return lambda: print('xxx')
f=f()
x=f()
print(x)
