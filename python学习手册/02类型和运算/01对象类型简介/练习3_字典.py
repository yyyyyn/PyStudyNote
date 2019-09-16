#字典
D={'food':'spam','quality':4,'color':'pink',1:'a'}

print('-----------字典 映射操作-------')
D['name']='Bob' #有则修改，无则添加
D['food']='rice'
print(D)
#显示
for k in D:
    print(k,'->',D[k],end=' ')
print()
print('----------字典 键的排序---------')
D=dict(a=1,c=3,b=2)
print(D)
#方式一：
ks=list(D.keys())
ks.sort()
for k in ks:
    print(k,'->',D[k],end=' ')
print()
#方式二：
for k in sorted(D):
    print(k,'->',D[k],end=' ')
print()

print('----------字典 查找in---------')
print('a' in D)
s=D['food'] if 'food' in D else 'unknow' #if/else的三元表达式
print(s)
