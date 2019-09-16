#使用列表，只能通过索引查看，不易查找
bob=['Bob Smith',42,30000,'software']
sue=['Sue Jones',45,40000,'hardware']
people=[bob,sue]
for p in people:
    print(p)

people.append(['Tom',50,0,None])
print(len(people))

bob=[['name','Bob Smith'],['age',42]]
sue=[['name','Sue Jones'],['age',45]]
people=[bob,sue]
for p in people:
    for (name,value) in p:
        if name=='name':print(value)

