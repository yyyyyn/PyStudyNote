'''
个人测试：以'https://hao.360.cn'为最初的网络，在其下所有url的标题中找出和关键字匹配的url

目前效果：极差，失败
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bfs
import re,random,datetime,time

home_host='https://hao.360.cn'
urldb={home_host}
urlnow={home_host}
urltemp=set()
urluseful=set()
reMatch1=re.compile(r'(钱|money)')
reMatch2=re.compile(r'^(http:|https:)\/\/.*')

def getLinks(host):
    print(host)
    global urldb,reMatch1,urluseful,urltemp
    html=urlopen(host)
    data=bfs(html,"html.parser")
    if data.find("title"):
        print('当前连接的标题是：',data.find("title").get_text())
        if reMatch1.match(data.find("title").get_text()) and host not in urluseful:
            urluseful.add(host)
    urlList=data.findAll(lambda tag: 'href'in tag.attrs and reMatch2.match(tag.attrs['href']))
    #print('urllist',urlList)
    for u in urlList:
        if u not in urldb:
            urltemp.add(u)

num=4
while num:
    print('this is the circle:',num)
    num-=1
    if not urlnow: break
    print('现在需要去检查',len(urlnow),'个url...')
    i=1
    print('aaa')
    #由于数据量太大，太慢，每一轮都只检查头10个
    for u in urlnow:
        if i>10 :break
        print('正在检查第',i,'个...')
        i+=1
        getLinks(u)
    urldb=urldb|urlnow
    urlnow=urltemp
    urltemp=set()
print('=========')
for u in urluseful:
    print(u)

