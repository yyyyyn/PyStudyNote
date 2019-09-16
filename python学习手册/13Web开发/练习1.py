'''
wsgi实现一个简单的web服务器
运行后在IE上输入网址：http://localhost:8000/xxxx
'''
from wsgiref.simple_server import make_server

#environ：一个包含所有HTTP请求信息的dict对象；
#start_response：一个发送HTTP响应的函数。
def application(environ,start_response):
    print(environ)
    start_response('200 OK',[('Content-Type','text/html')])
    body= '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:
httpd.serve_forever()