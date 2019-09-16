'''
导航树 ->通过位置找数据
1：找子标签，后代标签
子标签(children)就是一个父标签的直接下一级，而后代标签(descendants)是指一个父标签 下面所有级别的标签
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
data=bfs(html,"html.parser")

#打印giftList表格中所有产品的数据行(找出子标签:可以用 .children，后代标签可以用.descendants)：
#for child in data.find("table",{'id':'giftList'}).children:
#    print(child)

#找出某标签xx后面的兄弟标签next_siblings,但不包含xx，对象不能把自己当作兄弟标签
#for d in data.find("table",{"id":"giftList"}).tr.next_siblings:
#    print(d)

#找出父标签,previous_sibling:当前标签的前一个兄弟标签
d=data.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print(d)