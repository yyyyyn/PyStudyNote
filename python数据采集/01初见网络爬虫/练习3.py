'''
urlopen连接网络时可能会发生异常：
1.网页在服务器上不存在（或者获取页面的时候出现错误）--返回HTTP错误
2.服务器不存在--返回None

调用查询结果时：
如果你想要调用的标签不存在，BeautifulSoup 就会返回 None 对象。不过，
如果再调用这个 None 对象下面的子标签，就会发生 AttributeError 错误。

'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bfs
try:
    ht=urlopen("https://www.baidu.com")     #排除在网络连接过程中的错误
except HTTPError as e:
    print(e.__class__.__name__,e)
except Exception as e:
    print(e.__class__.__name__, e)
else:
    if ht:                      #排除ht为空的情况
        print('连接成功!')
        data=bfs(ht,"html.parser")
        print(data)
        #排除查找标签不存在的情况：
        try:
            r=data.body.div
        except AttributeError as e:
            print('标签未找到!')
        else:
            if r:
                print(r)
            else:
                print('标签未找到!')
    else:
        print('url找不到')

"=============================================="
