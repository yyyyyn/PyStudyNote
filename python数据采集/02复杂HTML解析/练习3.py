'''
正则表达式 及 Lambda表达式
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re

#a=re.match(r'^([A-Za-z0-9\._+]+)@([A-Za-z]+)\.(com|org|edu|net)$','zhang@qq.com')
testEmail=re.compile(r'^([A-Za-z0-9\._+]+)@([A-Za-z]+)\.(com|org|edu|net)$')    #匹配邮箱
a=testEmail.match('zhang@qq.com')
print(a.groups())

test2=re.compile(r'^((?![A-Z]).)*$')    #?!表示不包括，常放在最前面，本句表示不包括大写字符的任意字符串
a=test2.match('abc')
if a:
    print(a.groups())

print('===========在html数据筛选中使用正则表达式')
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
data=bfs(html,"html.parser")
testUrl=re.compile("\.\.\/img\/gifts/img.*\.jpg")
images=data.findAll('img',{'src':testUrl})
for image in images:
    print(image,image.attrs,image['src'])       #查找出img标签中的src内容

'''
对于一个标签myTag:
查看其所有属性:myTag.attrs 返回一个字典
查看其某项属性：myTag.attrs['src'] 或者 myTag['src']
'''

print('===========Lambda表达式筛选标签')
'''
BeautifulSoup 允许我们把特定函数类型当作 findAll 函数的参数。
会遍历所有标签(find只会用第一个)，依次把每个标签当作参数传给函数，要求返回一个布尔值做筛选
'''
tagList=data.findAll(lambda tag:len(tag.attrs)==2 and 'src' in tag.attrs)
for tag in tagList:
    print(tag)