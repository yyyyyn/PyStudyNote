#将数据写入本地文件中
dbfilename='data.txt'
ENDDB='enddb'
ENDREC='endrec.'
RECSEP='=>'

def storeDbase(db,dbfilename=dbfilename):
    "将数据库格式化保存文普通文件"
    dbf=open(dbfilename,'w')
    for key in db:
        print(key,file=dbf)
        for (name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbf)
        print(ENDREC,file=dbf)
    print(ENDDB,file=dbf)
    dbf.close()
def loadDbase(dbfilename=dbfilename):
    "解析数据，重构数据库"
    dbf = open(dbfilename, 'w+')
    import  sys
    sys.stdin=dbf
    db={}
    key=input()
    while key!=ENDDB:
        rec={}
        field=input()
        while field!=ENDREC:
            name,value=field.split(RECSEP)
            rec[name]=eval(value)
            field=input()
        db[key]=rec
        key=input()
    return db

if __name__=='__main__':
    loadDbase()
