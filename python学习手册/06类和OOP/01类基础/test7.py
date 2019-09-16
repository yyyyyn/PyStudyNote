x = 11

def f():
    print(x)

def g():
    x = 22
    print(x)

class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55

if __name__ == '__main__':
    # C.m.x='mm'
    print(C.m.x)