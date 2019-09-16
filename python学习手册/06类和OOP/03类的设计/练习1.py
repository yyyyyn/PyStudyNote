class A:
    def f1(self):
        print('abc')
    def f2():
        print('def')

def f3(self):
    print('ghi')
a=A()
a.f1()
A.f2()      #用类实例对象调用函数会默认发送给函数一个参数(self),用类对象则不会
f3(a)