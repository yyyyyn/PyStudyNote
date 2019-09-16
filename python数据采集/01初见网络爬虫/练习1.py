'''
内置模块:urllib
urlopen 用来打开并读取一个从网络获取的远程对象
'''
from urllib.request import urlopen
ht=urlopen('https://www.baidu.com')
data=ht.read()
print(type(ht),type(data),len(data))
print(data)
'''
当网络浏览器遇到一个标签时，比 如 <img src="cuteKitten.jpg">，
会向服务器发起另一个请求，以获取 cuteKitten.jpg 文件 中的数据为用户充分渲染网页。
但是，我们的 Python 程序没有返回并向服务器请求多个文 件的逻辑，
它只能读取我们已经请求的单个 HTML 文件。
'''