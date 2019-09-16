'''
TCP编程：
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议

IP地址可以用域名www.baidu.com自动转换到IP地址
作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把
端口号固定在80端口，因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，
FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了

接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，
直到recv()返回空数据，表示接收完毕，退出循环。
当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了

接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
'''
#客户端连接网络
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建Socket对象用于连接网络


s.connect(('www.baidu.com',80))                 #通过提供服务器的IP地址和端口号连接服务器

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n') #发送数据


#接受数据

buffer=[]
while True:
    d=s.recv(1024)  #每次最多接受1K
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()           #关闭连接


header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#把接受的数据写入文件
with open(r'd:/baidu.html','wb') as f:
    f.write(html)

