#元祖
T=(1,2,3,4)
print(T,T[1:3])   #支持索引切片
print('---------元祖 不可变列表-------')
T=(1,2,[3,4])
T[2][1]=22      #修改元祖中的列表，元祖中存的是列表的指针，并未改变
try:
    T[1]=12     #直接修改元祖中的内容，报错TypeError
except Exception as e:
    print(e.__class__.__name__)
print(T)
print('---------元祖 特有方法-------')
T=(1,1,2,3,4,5,5,5)
print(T.index(2))   #数值1第一次出现的位置
print(T.count(1))   #数值1出现的次数

#文件
print('---------文件 读写-------')
f=open('test.txt','w')  #手动打开文件
f.write('hello file\n')   #写入
f.write('hello file')
f.close()                 #关闭文件

f=open('test.txt')
print(f.read())            #一次性读取所有内容
f.close()

print('---------文件 文件迭代器读取-------')
for l in open('test.txt'):#使用完会自动关闭文件
    print(l,end='')