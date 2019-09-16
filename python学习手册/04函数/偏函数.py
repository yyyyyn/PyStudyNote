'''
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义，可以直接创建一个新的函数
'''
import functools
int2=functools.partial(int,base=2)
print(int2('100000'))