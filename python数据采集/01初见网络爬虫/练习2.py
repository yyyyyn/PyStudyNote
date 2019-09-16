'''
外部模块BeautifulSoup
安装:pip install beautifulsoup4
BeautifulSoup 尝试化平淡为神奇。它通过定位 HTML 标签来 格式化和组织复杂的网络信息，
用简单易用的 Python 对象为我们展现 XML 结构信息。

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
html=urlopen("https://www.baidu.com/")
bsObj=bfs(html, "html.parser")  #"html.parser"表示解析器，默认是这个
#下面两个效果是一样的,通过标签查找，返回一个标签的内容
print(bsObj.html.head.script)
print(bsObj.script)