#函数中用return跳出多层循环
def f():
    while True:
        while True:
            s=input("Enter a word:")
            if s=='stop':
                return
    print('aaa')

f()

#设置判断标志跳出循环
print('------------------')
flag=False
while True:
    if flag:
        break
    while True:
        s=input('Enter a string:')
        if s=='stop':
            flag=True
            break