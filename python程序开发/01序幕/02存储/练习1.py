#可以将数据直接存储在脚本中
#记录
bob=dict(name='Bob Smith',age=42,pay=30000,job='dev')
sue=dict(name='Sue Jones',age=45,pay=4000,job='hdw')
tom=dict(name='Tom',age=50,pay=0,job=None)

#数据库
db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

#测试
if __name__=='__main__':
    for k in db:
        print(k,db[k])