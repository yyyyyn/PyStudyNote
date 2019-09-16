'''
个人测试：在所给的一个小说网站中找出所有的小说
https://www.dawenxue.net/

soup=bfs(...)遇到编码问题：
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
这是由于少数页面编码问题导致的，解决方案如下(也可添加参数from_encoding="iso-8859-1")

目前效果：一般
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re

re1=re.compile(r'.*第.*章.*')
host=r"https://www.dawenxue.net"

soup=bfs(urlopen(host).read().decode('utf-8','ignore'),"html.parser")
bookList=soup.findAll("a",{'target':'_blank'})
d=set()
for book in bookList:
    text=book.get_text()
    if 'style' not in book.attrs and not re1.match(text):
        d.add(text)
d.remove('')
for data in d:
    print(data)