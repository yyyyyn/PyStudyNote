from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()                          # 创建对象的基类:
class User(Base):                               # 定义User对象
    __tablename__='zj_user'                     #对应的数据库中表的名称
    #表的结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
# 初始化数据库连接:
engine=create_engine('mysql+mysqlconnector://root:0000@localhost:3306/zj_test')
DBSession=sessionmaker(bind=engine)             # 创建DBSession类型:

"插入数据"
session=DBSession()   # 创建session对象
new_user=User(id='4',name='Ddd')               # 创建新User对象
try:
    session.add(new_user)                           # 添加到session
    session.commit()                                # 提交即保存到数据库
    print('插入数据成功!')
except:
    print('插入失败!')
finally:
    session.close()                                 # 关闭session

"查询数据"
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
users = session.query(User).filter(User.id=='1').all()
# 打印类型和对象的name属性:
print('type:', type(users),type(users[0]))
for u in users:
    print(u.id,u.name)
session.close()