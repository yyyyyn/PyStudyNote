def f():
    for i in range(10):
        yield i

for i in f():
    print(i,end=' ')
print()

print('扩展生成器函数协议：send和next')
def f():
    print('aaaa')
    for i in range(100,200):
        print('bbbb')
        x=yield i
        print('x given to f() is : ',x)

f=f()                             #这里不会执行
for i in range(8):
    print('for',i)
    data=i if i>0 else None     #生成器函数第一次执行要send(None)
    result=f.send(data)
    print('outer',result)