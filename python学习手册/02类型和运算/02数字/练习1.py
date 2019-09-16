a,b,c,d='0b111','0o123',123,'0x123'
print('===================十进制转2/8/16进制')
print('原数据:',c,'转换后:',bin(c),oct(c),hex(c))
print('原数据类型:',type(c),'转换后类型:',type(bin(c)),type(oct(c)),type(hex(c)))
#2/8/16进制间计算要先转换，不然只是字符串的计算
print('0b11'+'0b11',int('0b11',2)+int('0x11',16))

import os
if os.path.exists('知识点.txt'):
    os.remove('知识点.txt')

print('===================浮点数,小数类，分数类')
import decimal
from fractions import Fraction
a,b=.13442,1.12312
print('a+b=',a+b)
decimal.getcontext().prec=9         #设置小数保留位数
print('a+b=',decimal.Decimal(a)+decimal.Decimal(b))
with decimal.localcontext() as ctx: #临时重置小数精度,退出with后变为默认
    ctx.prec = 2
    print(decimal.Decimal('1.0')/decimal.Decimal('3.0'))
print(decimal.Decimal('1.0')/decimal.Decimal('3.0'))
print('a+b=',decimal.Decimal('.13442')+decimal.Decimal('1.12312'))
print('还可以这样控制精度:','%.2f'%a,'{0:.2f}'.format(a))

f1,f2=Fraction(1,2),Fraction(2,3)
print(f1,'+',f2,'=',f1+f2)
print('===================复数')
a=2+3j
b=complex(3,4)
print(a,'+',b,'=',a+b)

print('===================除法')
import math
print(5/2, 4/2, 4.0/2, 4/2.0)               #普通除法
print(5//2, 5.0//2, 5//2.0, 5.0//2.0, -5//2)#真除法(效果类似math.floor())
print(math.floor(2.5),math.floor(-2.5))     #floor取整(向下舍入)
print(math.trunc(2.5),math.trunc(-2.5))     #截断取整

print('===================位操作')
d='0xabcde'
print(hex(int(d,16)<<8))    #往左移动八位，相当于乘以2的八次方

print('===================数学工具')
import random,datetime
random.seed(datetime.datetime.now())    #每次随机选择前都会默认调用seed,设置不同的seed有助于随机效率
print(random.choice([1,2,3,4]))
print(random.randint(1,10))
