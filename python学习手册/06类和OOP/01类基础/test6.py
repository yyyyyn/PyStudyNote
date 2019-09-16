from abc import ABCMeta, abstractclassmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractclassmethod
    def action(self):
        pass
# x = Super() #TypeError: Can't instantiate abstract class Super with abstract methods action

class Sub(Super):
    pass
# x = Sub() #TypeError: Can't instantiate abstract class Sub with abstract methods action

class Sub(Super):
    def action(self):
        print('sub action')

x = Sub()
x.delegate()