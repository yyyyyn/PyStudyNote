'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，
所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。

Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
'''
import sqlite3 as db

conn=db.connect('testsqllite.db')
cur=conn.cursor()
cur.execute('create table if NOT EXISTS user (id varchar(20) primary key, name varchar(20))')
try:
    cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cur.execute("insert into user (id, name) values ('1', 'Michael')")
    cur.execute("insert into user (id, name) values ('2', 'Alices')")
except Exception as e:
    print(e.__class__.__name__)
#cur.execute("update user set name='Bob' where id='1'")
cur.execute("delete from user where id='3'")

#cur.execute('select * from user where id>=?', ('1',))
values = cur.fetchall()
print(type(values))
print(values)
cur.close()
conn.commit()
conn.close()

