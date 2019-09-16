'''
学校服务器，录入学校数据
1.首先运行server代码，完善后台数据结构
'''

import socket
import sqlite3 as db
import threading

lock=threading.Lock()
def tcplink(sock,addr):
    conn = db.connect('test3.db')
    cur = conn.cursor()
    while True:
        try:
            data=(sock.recv(1024)).decode('utf-8')
            if not data: break
            lock.acquire()
            try:
                cur.execute(data)
            finally:
                lock.release()
            conn.commit()
            values = cur.fetchall()
            if values:
                sock.sendall(repr(values).encode('utf-8'))
            else:
                sock.send('操作成功'.encode('utf-8'))
        except Exception as e:
            sock.send((e.__class__.__name__).encode('utf-8'))
    cur.close()
    conn.commit()
    conn.close()
    sock.close()
    print('结束本次登陆操作!')

conn=db.connect('test3.db')  #若test.db不存在会自动创建
cur=conn.cursor()
cur.execute("create table if not EXISTS user(id varchar(20),name varchar(20))")
cur.close()
conn.commit()
conn.close()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.3',9999))
s.listen(10)
print('The server is beging to work...')
while True:
    sock,addr=s.accept()
    print('A client is link to the server...')
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


