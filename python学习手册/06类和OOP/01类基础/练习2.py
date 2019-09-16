class A:
    def __int__(self,name):
        self.name=name

class B(A):
    def __init__(self,age):
        self.age=age

b1=B(23)
print(b1.age)
try:
    print(b1.name)
except Exception as e:
    print(e)