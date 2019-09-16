'''
给出一个页面链接"http://oreilly.com"
从中随机找出一个外链，返回，再打开该外链，随机找出其中一个外链，再返回，重复该过程
如果某个页面下没有外链就随机打开其中的一个内链，再找外链，没有就再打开内链来找外链，直到找到，返回，重复上述过程
上述过程直到页面中既没有外链也没有内敛及结束
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,datetime,random

pages = set()
random.seed(datetime.datetime.now())

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头或包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面中一个由内链打开的页面中的外链
def getNextExternalLinks(innerList):
    externalLinks=[]
    bsObj=BeautifulSoup(urlopen(innerList),"html.parser")
    for link in bsObj.findAll("a",href=re.compile("^(http|www).*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,"html.parser")
    addressParts=splitAddress(startingPage)
    externalLinks = getExternalLinks(bsObj, addressParts[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj,"/".join(addressParts[1:]) if len(addressParts)>1 else '')
        return getNextExternalLinks(addressParts[0]+internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    if externalLink:
        print("随机外链是： " + externalLink)
        followExternalOnly(externalLink)

#followExternalOnly("http://oreilly.com")

print('====================扩展')
# 收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
        print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是： " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


getAllExternalLinks("http://oreilly.com")
