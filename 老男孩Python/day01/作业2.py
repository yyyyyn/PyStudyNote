'''
三级菜单
可以依次选择进入各个子菜单
'''
D={'中国菜':{'川菜':{'a':'麻婆豆腐','b':'水煮鱼'},'鲁菜':{'a':'东坡肘子'}},'日本菜':'寿司'}
while True:
    print('请问喜欢吃哪个国家的菜，我们的选择有:')
    for k in D:
        print(k,end =' ')
    print()
    choice1=input('我选择：')
    d2=D[choice1]
    print('请问喜欢吃哪个菜系的菜，我们的选择有:')
    for k in d2:
        print(k,end =' ')
    print()
    choice2 = input('我选择：')
    d3=d2[choice2]
    print('我们的菜品有：')
    for k in d3:
        print(k,'->',d3[k],end=' ')
    print()
    choice3=input('我选择:')
    print('您点了本店的特色菜{0}!'.format(d3[choice3]))
    choice4=input('先生请问还需要什么服务(1:继续点菜 2：停止点菜)?')
    if choice4=='2':
        print('好的先生，我们将一会儿为您送到!')
        break


