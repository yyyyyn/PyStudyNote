l=[]
l.append(1)
l.append([11,111])
l.extend([2,3])
l.insert(9,[4,5])
print(l)

l.pop(1)
l.remove([4,5])
del l[:1]
l[0]=123
print(l)