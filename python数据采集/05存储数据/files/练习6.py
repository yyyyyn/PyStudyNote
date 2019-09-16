'''
找出基维百科某个词条索引下的标题和第一段内容存入数据库，再在其中找一个词条打开重复之前过程，一直进行下去
效果相当于在基维百科页面中不停点击词条，浏览网页
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re,datetime,random
import pymysql as db

random.seed(datetime.datetime.now())
conn=db.connect(host='127.0.0.1',user='root',passwd='0000',db='pypagedb',charset='utf8mb4')
cur=conn.cursor()
reMatch=re.compile("^(/wiki/)((?!:).)*$")

def store(title,content):
    if len(title)>10: title=title[:10]
    if len(content)>20: content=content[:20]
    sql="insert into pages(id,mc)values('%s','%s')" % (title,content)
    try:
        cur.execute(sql)
    except Exception as e:
        print(e)
        print('保存失败!')
    cur.connection.commit()

def getLinks(articleUrl):
    html= urlopen("http://en.wikipedia.org"+articleUrl)
    data=bfs(html,"html.parser")
    title=data.find("h1").get_text()
    content=data.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return data.find("div",{"id":"bodyContent"}).findAll("a",href=reMatch)

try:
    links = getLinks(r'/wiki/Kevin_Bacon')
    while links:
        aUrl=links[random.randint(0,len(links)-1)].attrs["href"]
        print('进入链接：',"http://en.wikipedia.org"+aUrl)
        links=getLinks(aUrl)
except:
    print('出现错误')
finally:
    cur.close()
    conn.close()
