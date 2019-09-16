'''
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，
递归调用的次数过多，会导致栈溢出。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，
不会出现栈溢出的情况。

'''
#递归
def f1(n):
    if n==1:
        return n
    else:
        return n+f1(n-1)

#尾递归
def f2(n):
    return f2_iter(n,1)
def f2_iter(num,result):
    if num==1:
        return result
    else:
        return f2_iter(num-1,result+num)

if __name__=='__main__':
    print(f1(5))
    print(f2(5))