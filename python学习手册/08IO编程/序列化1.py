'''
我们把变量从内存中变成可存储或传输的过程称之为序列化
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，
而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象
'''
import json
d=dict(name='Bob',age=20,score=68)
j=json.dumps(d)                     #dumps()方法返回一个str，内容就是标准的JSON
print(j)
print(json.loads(j))                #JSON的字符串反序列化


#序列化类,需要有专门的方法来定义输出
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def getStudent(s):
    return {
        'name':s.name,
        'age':s.age
    }
stu=Student('Bob',24)
j=json.dumps(stu,default=getStudent)
print(j)
print(json.dumps(stu,default=lambda s:s.__dict__))