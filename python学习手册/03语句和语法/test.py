try:
    print(1/3)
except Exception as e:
    print(e)
else:
    print('ccc')

l=[1,2,3]
i=iter(l)
print(next(i))
d=(x for x in [1,2,3])
print(next(d))

c={1,2,3}
for k in c:
    print(k)

print('=======')
l=[1,2,3]
i=iter(l)
for k in i:
    print(k)