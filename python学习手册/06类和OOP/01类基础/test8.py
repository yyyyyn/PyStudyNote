'''
查找类的所有超类直到顶层
'''
def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for c in cls.__bases__:
        classtree(c, indent+3)
def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    # instancetree(F())

if __name__ == '__main__':
    selftest()