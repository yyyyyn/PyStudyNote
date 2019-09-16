'''
Python对协程的支持是通过generator(生成器yield)实现的。
'''
def consumer():
    print('0020')
    r = 'xxx'
    while True:
        print('0021')
        #运行周期：[开始...yield r][n=1...yield r][n=2...yield r]...
        n = yield r
        print('0022', n, r if r else 'None')
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    #生成器第一次执行不能传送值，只能用None，开始c的次一次运行周期：
    print('0010')
    rr = c.send(None)
    print('rr is:', rr if rr else 'None')
    print('0030')
    n = 0
    while n < 3:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)       #相当于调用函数，欸一次就是一个c的运行周期
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()  #这是一个生成器，与函数是有区别的，这样不会执行其中代码，后面send()触发执行或者next
print(type(c))
produce(c)

