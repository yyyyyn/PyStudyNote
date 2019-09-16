class A:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name

a1=A('Alice')
print(a1.name)

a1.name='Bob'
print(a1.name)
