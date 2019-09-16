#集合
print('--------集合set--------')
X=set('spam')
X.add('a')
X.add('ss')
print(X)
print('{}的类型是',type({}))

print('-------浮点数Decimal--------')
"decimal和Fraction可以用来解决浮点数的不精确性"
import decimal
print(3.1415+1)
d=decimal.Decimal('3.1415')
print(d+1)
print(r'1/3的结果是：',1/3)
decimal.getcontext().prec=4     #设置decimal小数点保留位数
print(r'使用decimal后1/3的结果是：'
      ,decimal.Decimal('1')/decimal.Decimal('3'))

print('-------十进制数Fraction--------')
from fractions import Fraction
f=Fraction(2,3)                 #三分之二
print(f+1)
print(f+Fraction(1,2))

print('-------布尔值--------')
print(bool('spam'),bool({}))

print('--------None--------')
x=None
print(bool(x),[x]*4)