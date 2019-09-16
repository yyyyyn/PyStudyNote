'''
xml解析工具
'''
print('=========使用re模块查找')
import re
text=open('mybooks.xml').read()
found=re.findall('<title>(.*)</title>',text)
print(type(found))
for title in found: print(title)

print('=========为了更加稳健，使用DOM解析')
from xml.dom.minidom import parse,Node
xmltree=parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType==Node.TEXT_NODE:
            print(node2.data)

print('=========SAX解析XML')
import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle=False
    def startElement(self,name,attributes):
        if name=='title':
            self.inTitle=True
    def characters(self,data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name=='title':
            self.inTitle=False
import xml.sax
parser=xml.sax.make_parser()
handler=BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')

print('=========etree解析XML')
from xml.etree.ElementTree import parse
tree=parse('mybooks.xml')
for E in tree.findall('title'):

    print(E.text)