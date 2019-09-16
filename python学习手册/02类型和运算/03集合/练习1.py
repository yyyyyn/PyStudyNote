c=set()
l=[1,2]
try:
    c.add(l)
except Exception as e:
    print(e)

c.add('a')
c.update('b')
c.update(['c','d'])
c.update(set(['e','f']))
c=c.union(['g','h'])
c=c.union(set(['i','j']))
print(c)

c1={'a','b'}
print(c&c1)