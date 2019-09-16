#内置异常类构造函数中包括一个元祖可用于传递数据
class E(Exception): pass

try:
    raise E('spam')
except E as x:
    print(x,x.args)

try:
    raise E('spam','eges','ham')
except E as x:
    print(x,x.args)