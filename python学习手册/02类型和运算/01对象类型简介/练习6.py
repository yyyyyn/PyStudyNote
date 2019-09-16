print('-----------type---------')
#type 类型检测
L=[1,2,3]
print(type(L))
print(type(type),type(type(L)))
if type(L)==type([]):
    print('yes1')
if type(L)==list:
    print('yes2')
if isinstance(L,list):
    print('yes3')

print('-----------类---------')
class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def __str__(self):
        return '{0} name:{1},pay:{2}'.format(self.__class__.__name__,self.name,self.pay)

w=Worker('bob',1000)
print(w)