#列表
print('---------列表 序列操作')
L=[123,'sapm',1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L+[1,2,3])
print('---------列表 特定操作-----')
L.append('NI')      #添加在末尾
print(L)
L.pop(2)            #按索引删除,返回被删除项
print(L)
M=['b','a','c']
M.sort()            #排序ASC,内容要是相同格式
print(M)
M.reverse()         #倒叙
print(M)
print('---------列表 边界检查-----')
try:
    print(L[len(L)+1])
except Exception as e:
    print(e.__class__.__name__)#超出边界报错IndexError

print('---------列表 嵌套-----')
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M[1],M[1][1])
md=['apsm',1,[2,3],(4,5),{'a':12}]
print(md)

print('---------列表 列表解析-----')
M=[[1,2,3],[4,5,6],[7,8,9]]
print([i[1] for i in M if i[1]>2])
print([M[i][i] for i in [0,1,2]])
print([i*2 for i in 'spam'])
print({sum(r) for r in M})              #当外层是大括号时，根据内容可以用来创建集合
print({i:sum(M[i]) for i in range(3)})  #当外层是大括号时，根据内容可以用来创建字典

G=(sum(r) for r in M)                   #当外层是括号时，创建的是生成器，用于迭代
print(G)
for g in G:
    print(g)
try:
    print(next(G))
except Exception as e:
    print(e.__class__.__name__)
