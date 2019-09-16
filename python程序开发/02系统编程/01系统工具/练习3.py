L=[1,2,3,4]
s='abcd'

s=s.replace('a','A')
print(s)

s='B'.join(s.split('b'))
print(s)

l=list(s)
for i in range(len(l)):
    if l[i]=='c':
        l[i]='C'
s=''.join(l)
print(s)
