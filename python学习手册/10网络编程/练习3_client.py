import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('192.168.1.3',9999))
while True:
    print('''choase what you want to do:1:add 2:delete 3:update 4:select 5:exit''')
    chose=input('Enter your choice:')
    if chose=='1':
        id=input('input your id:')
        name=input('input your name:')
        orders="insert into user(id,name)values('%s','%s')"%(id,name)
    elif chose == '2':
        ids=input('Input the id that you want to delete:')
        orders="delete from user where id='%s'"%ids
    elif chose == '3':
        ids=input('Input the id that you want to update:')
        names=input('Input the name that you want it to be:')
        orders="update user set name='%s' where id='%s'"%(names,ids)
    elif chose=='4':
        orders="select id,name from user"
    elif chose=='5':
        print('This is the end!')
        break
    else:
        print('chose again!')
        continue
    c.send(orders.encode('utf-8'))
    #print(c.recv(1024).decode('utf-8'))
    buf=[]
    flag=True
    while flag:
        d=c.recv(1024)
        buf.append(d)
        if len(d)<1024: flag=False
    result=(''.encode('utf-8')).join(buf)
    print(result.decode('utf-8'))
c.close()