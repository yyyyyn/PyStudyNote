import mysql.connector as db
conn = db.connect(user='root', password='0000', database='zj_test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table if not EXISTS zj_user (id varchar(20) PRIMARY KEY , name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
#cursor.execute('insert into zj_user (id, name) values (%s, %s)', ['1', 'Michael'])
#print('rowcount is:',cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from zj_user where id >= %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()