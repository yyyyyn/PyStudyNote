print('==========在模块中隐藏数据,查找数据')
import test1,sys
print(test1.__dict__['y'])
print(test1.__all__)
print(test1._x)
print(getattr(test1,'y'))
print(sys.modules['test1'].y)