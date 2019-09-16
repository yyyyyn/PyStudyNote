from datetime import date,datetime
t1=datetime.now()
print(t1,type(t1))

t2=datetime(2017,2,12,12,2,2,12)    #最少三个(年月日)最多七个(年月日时分秒毫秒)
print(t2)

print('datetime转换为timestamp(计算机内存储的标准时间)')
tt=t2.timestamp()
print(tt)

print('timestamp转换为datetime')
t3=datetime.fromtimestamp(tt)
print(t3,type(t3))

print('时间加减可以直接用+和-运算符，不过需要导入timedelta这个类')
from datetime import timedelta
t4=datetime.now()
t5=t4-timedelta(days=1)
print(t4,t5,type(t5))