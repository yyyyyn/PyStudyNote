class Indexer:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        tmp = list(self.data)
        tmp[key] = list(value)[0]
        self.data=''.join(tmp)

def test_indexer():
    t = Indexer('abcde')
    print(t[0], t[1:4])
    t[2] = 'r'
    print(t[2])
    for s in t:
        print(s, end = ' ')
    print('...')

class Squares:
    def __init__(self, start, stop):
        self.value = start -1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2

def test_squares():
    for i in Squares(1,5):
        print(i, end = ' ')
    x = Squares(1, 5)
    it = iter(x)
    for r in range(4):
        print(next(it) ,end=' ')
    print('...')

class SquaresObject(Squares):
    def __iter__(self):
        return Squares(self.value, self.stop)

def test_SquaresObject():
    s = Squares(1,4)            #单迭代对象
    s2 = SquaresObject(1, 4)    #多迭代对象
    for j in s:
        for k in s:
            print(j, k, end='| ')
    print('')
    for j in s2:
        for k in s2:
            print(j, k, end='| ')
    print('...')

class C:
    def __index__(self):
        return 255

def test_c():
    x = C()
    print(hex(x), bin(x), oct(x))
    print(('c' * 256)[x], '...')   #在需要一个整数的环境中应用，包括索引

if __name__ == '__main__':
    print('test __getitem__ and __settime__:')
    test_indexer()
    print('test __item__ and __next__:')
    test_squares()
    test_SquaresObject()
    print('test __index__:')
    test_c()