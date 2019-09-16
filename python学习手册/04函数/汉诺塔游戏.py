'''
汉诺塔游戏：
有三个柱子，A,B,C,A中从上往下，从小到大重叠有N个盘子，借助B将A中的盘子照样移动到C中，
在移动过程中盘子的重叠都是上面下下面大
'''
def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(4,'A',"B",'C')