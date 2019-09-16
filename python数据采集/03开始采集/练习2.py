'''
采集整个网站:
从顶级页面开始（比如主页），然后搜索页面上的所有链接，形成列表。再去采集这些链接的每一个页面，
然后把在每个页面上找到的链接形 成新的列表，重复执行下一轮采集（注意重复了的链接要去重）。

这里采用递归的方式收集，但如果网站链接太多（1000+），会导致速度越来越慢直到崩溃
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re,datetime,random

random.seed(datetime.datetime.now())        #定义随机数种子
reTest1=re.compile("^(/wiki/)((?!:).)*$")
page=set()
def getLinks(pageUrl):
    global page
    global reTest1
    try:
        html=urlopen(r"http://en.wikipedia.org"+pageUrl)
        soup = bfs(html, "html.parser")
    except Exception as e:
        print(e)
        return  None

    try:
        print(soup.h1.get_text())  # 打印标签元素
    except Exception as e:
        print(e)

    try:
        result= soup.find("div",{"id":"bodyContent"}).findAll("a",href=reTest1)
    except Exception as e:
        print(e)
        return None
    for link in result:
        if 'href' in link.attrs:
            if link.attrs['href'] not in page:
                newPage=link.attrs['href']
                print(newPage)
                page.add(newPage)
                getLinks(newPage)
    return None

getLinks("")
for d in page:
    print(d)
