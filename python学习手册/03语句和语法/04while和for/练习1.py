#!/usr/local/bin/evn python
# -*- coding: UTF-8 -*-

print('range和分片')
print(list(range(0,10,2)))

while True:
    j=10
    while j:
        print('j is: ',j)
        j-=1
        if j<5:
            break
    print('while true end')
    break

print('产生偏移和元素enumerate')
for (offset,item) in enumerate('abcd'):
    print(offset,item)

# for r in open('知识点.txt'):
#     print(r, end='')