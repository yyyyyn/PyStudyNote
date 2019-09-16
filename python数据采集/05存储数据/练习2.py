'''
把 http://pythonscraping. com 主页上所有 src 属性的文件都下载下来
'''
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bfs
import os

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

#根据url链接和找出的所有的src数据来匹配出最正确合理有效的url并返回
def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url

#返回下载文件保存路径，若没有就创建一个空的
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = bfs(html,"html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
#urlretrieve:这里是把给出的url指向的数据下载下来保存到所给文件中
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
