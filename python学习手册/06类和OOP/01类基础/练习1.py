class A:
    num=0
    def __init__(self,name):
        self.name=name

a=A('Bob')
print(a.__dict__)
print(dir(a))
print(a.num)
A.num+=1
a2=A('Alice')


print(a2.num)