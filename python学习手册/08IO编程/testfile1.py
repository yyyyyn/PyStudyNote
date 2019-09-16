f=open(r'd:/a.txt','w')
f.write('hello file')
f.close()

f=open(r'd:/a.txt')
print(f.read())
f.close()