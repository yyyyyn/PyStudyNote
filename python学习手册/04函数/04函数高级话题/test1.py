from collections import Iterable


def sum_seq(*seq):
    "纯数字的数字，列表，元祖，集合，字符串求和"
    sum = 0
    for s in seq:
        "单个字符仍是可迭代对象，在这里用len(s)>1预防进入死循环"
        sum = sum + sum_seq(*s) if isinstance(s, Iterable) and len(s) > 1 else sum + int(s)
    return sum

print(sum_seq([1,2,3,[4,5]],{6,7},(8,9)))


def f(a: 'spam' = 4, b: (1, 10) = 5) -> int:
    print(a, b)

f()
print(f.__annotations__)

lambda x=1: x**2
