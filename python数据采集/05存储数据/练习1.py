'''
可以只存储url，不过这样风险大，url可变性大(被防盗或改变)，却小而快且容易，可以用于那些不重要或一次性的链接

在 Python 3.x 版本中，urllib.request.urlretrieve 可以根据文件的 URL 下载文件
'''
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bfs

html=urlopen('http://www.pythonscraping.com')
soup=bfs(html,"html.parser")

#下载一个logo图标保存到本地
imageLocation=soup.find("a",{"id":"logo"}).find("img")['src']
urlretrieve(imageLocation,"logo.jpg")