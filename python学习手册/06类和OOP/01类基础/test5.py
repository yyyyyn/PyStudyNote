class Super:
    def method(self):
        print('Super method ...')
    def delegrate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('Replacer method ...')

class Provider(Super):
    def action(self):
        print('Provider action ...')

if __name__ == '__main__':
    for c in (Super, Inheritor, Replacer, Provider):
        print(c.__name__)
        c().method()
    Provider().delegrate()