'''
为枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
'''
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar'))
print(Month,Month.Jan)
for name,member in Month.__members__.items():
    print(name,'->',member,'#',member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数