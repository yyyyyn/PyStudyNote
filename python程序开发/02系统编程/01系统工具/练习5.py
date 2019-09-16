import  sys,traceback
def f():
    raise TypeError('already got one')
try:
    f()
except:
    #traceback.print_exc()
    "print_exc也能显示最近异常"
    t,v,tb=sys.exc_info()
    "exc_info方法返回一个元祖包括(异常类，异常类实例，traceback对象"
    print(t)
    print(v)
    traceback.print_tb(tb)