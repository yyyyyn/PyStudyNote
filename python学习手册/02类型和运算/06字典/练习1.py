print(dict(a=1,b=2))
print(dict.fromkeys(['a','b']))
print(dict(zip(['a','b'],[1,2])))

d=dict(zip(['a','b'],[1,2]))
print(type(d.keys()),d.keys(),list(d.keys()))
print(d.get('c','unknow'))

print( dict([('name','bob'),('age',23)]) )

#排序
for k in sorted(d):
    print(k,d[k])