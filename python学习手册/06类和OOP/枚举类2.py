from enum import Enum,unique

#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
for name in Weekday:
    print(name)