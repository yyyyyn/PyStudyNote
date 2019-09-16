#嵌套结构
bob={'name':{'first':'Bob','last':'Smith'},
     'age':42,
     'job':['software','writing'],
     'pay':(40000,50000)}

print(bob['name'])
print(bob['name']['last'])

#字典的字典
bob=dict(name='Bob Smith',age=42)
sue=dict(name='Sue Jones',age=45)
db={}
db['bob']=bob
db['sue']=sue

print(db)

#内置模块pprint,使输出更容易理解
import pprint
pprint.pprint(db)