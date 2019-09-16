'''
将数据存入Mysql数据库
在进行网络数据采集时，处理 Unicode 字符串是很痛苦的事情。默认情况下，MySQL 也 不支持 Unicode 字符处理。不过可以设置:
ALTER DATABASE pypagedb CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;   #数据库支持
ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  #表支持
ALTER TABLE pages CHANGE id id VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;   #列支持
ALTER TABLE pages CHANGE mc mc VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;   #列支持

'''
import pymysql as db
import pprint
conn=db.connect(host='127.0.0.1',user='root',passwd='0000',db='pypagedb',charset='utf8mb4')
cur=conn.cursor()
print('seccessful to link to mysql...')

sql2="delete from pages"
sql4="select id,mc from pages"
try:
    while True:
        print('1234/5:增删改查/退出')
        chose=input('请选择:')
        if chose=='5': break
        if chose=='2':
            cur.execute(sql2)
        if chose=='4':
            cur.execute(sql4)
            pprint.pprint(cur.fetchall())
except:
    print('出错!')
finally:
    cur.close()
    conn.commit()
    conn.close()
