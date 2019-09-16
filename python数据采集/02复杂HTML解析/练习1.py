'''
findAll函数特定查找->通过标签找数据
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs

ht=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
data=bfs(ht.read(),"html.parser")

# findAll 函数抽取所有包含在 <span class="green" ...></ span> 标签里的文字,返回列表
namelist=data.findAll(['span','h1'],{'class':'green'})
for l in namelist:
    print(l,'---',l.get_text())
    #返回的列表包含标签信息，可以用get_text()过滤标签及其中的链接等，只保留文本

'''
findAll与find: find相当于findAll中的limit=1,只返回第一条结果
findAll(tag, attributes, recursive, text, limit, keywords) 
find(tag, attributes, recursive, text, keywords)

tag:传一个标签的名称或多个标签名称组成的列表或集合做标签参数 {"h1","h2"}
attributes 是用一个字典封装一个标签的若干属性和对应的若干属性值 {"class":{"green", "red"}})
recursive是一个布尔变量。表示抓取HTML文档标签结构里多少层的信息，默认是全部
text有点不同，它是用标签的文本内容去匹配 xx.findAll(text="the prince") 
limit:结果标签的数量
keyword：可以让你选择那些具有指定属性的标签  bsObj.findAll(id="text") 
'''

'''
BeautifulSoup库对象：
 BeautifulSoup对象 ：上述data
 标签Tag对象 通过 find 和 findAll，或者直接调用子标签获取的一列对象或单个对象
 NavigableString对象 用来表示标签里的文字，不是标签
 Comment对象 用来查找 HTML 文档的注释标签，<!-- 像这样 -->
'''