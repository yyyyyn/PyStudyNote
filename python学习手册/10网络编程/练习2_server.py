import socket
import threading
import time
from datetime import datetime

def tcplinks(sock,addr):
    t=datetime.now()
    print(t)
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'welcome!')
    while True:
        data=sock.recv(1024)
        #print(data.decode('utf-8'))
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('hello,%s!'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed'%addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection...')
while True:
    sock,addr=s.accept()
    #print(type(sock),type(addr),sock,addr)
    t=threading.Thread(target=tcplinks,args=(sock,addr))
    t.start()


