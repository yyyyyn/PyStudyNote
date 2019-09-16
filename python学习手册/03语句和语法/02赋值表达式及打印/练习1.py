print('################## 赋值 ##################')
a, b, c = range(3)
print(a, b, c)      #1 2 3
a,*b = range(3)
print(a, b)         #0 [1, 2]
a, *b, c = range(6)
print(a, b, c)      #0 [1, 2, 3, 4] 5
l = [1,2,3,4]
while l:
    f, *l = l
    print(f, l)     #1 [2, 3, 4] \n 2 [3, 4] n 3 [4] \n 4 []

l1=l2=[1,2,3]
print(l1, l2, l1 is l2) #True
l1+=[4,5]       #
print(l1, l2, l1 is l2) #True
l2=l1+[6,7]
print(l1, l2, l1 is l2) #False

import sys
#print('abc',file=open('testprint.txt','w'))
#sys.stdout.write('hello wirld')     #与print效果一样

#输出流重定向
temp=sys.stdout
sys.stdout=open('testprint.txt','a')    #设置打印的位置
print('abc')
print('12312')
#sys.stdout.flush()
sys.stdout.close()      #关闭,保存之前的数据
sys.stdout=temp         #将打印位置换回来
print('asdfaf')

sys.stderr.write('bad!' * 8 + '\n') #打印标准错误流

