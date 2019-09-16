'''
遍历单个域名
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re,datetime,random

random.seed(datetime.datetime.now())        #定义随机数种子
reTest1=re.compile("^(/wiki/)((?!:).)*$")

def getLinks(values):
    global reTest1
    try:
        print('Linking to:',r"http://en.wikipedia.org"+values,' ,please waiting...')
        html=urlopen(r"http://en.wikipedia.org"+values)
    except Exception as e:
        print(e)
        return None

    soup=bfs(html,"html.parser")

    try:
        result= soup.find("div",{"id":"bodyContent"}).findAll("a",href=reTest1)
    except Exception as e:
        print(e)
        print('Can not get useful data!')
        return None

    return result

links=getLinks(r"/wiki/Kevin_Bacon")
times=3
while times and links:
    times-=1
    newValue=links[random.randint(0,len(links)-1)].attrs['href']
    print(newValue)
    links=getLinks(newValue)
