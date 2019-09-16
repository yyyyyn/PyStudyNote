'''
实现目录下查找指定文件(包括子目录)
'''
import os
#在路径下查找文件
def findFile2(dirname,filename):
    D={};L=[dirname]
    while L:
        L1=[]
        for l in L:
            values = [x for x in os.listdir(l) if os.path.isfile(os.path.join(l, x)) and filename in os.path.splitext(x)[0]]
            if values:  D[l] = values
            L1.extend([os.path.join(l,x) for x in os.listdir(l) if os.path.isdir(os.path.join(l,x))])
        L=L1
    return D
if __name__=='__main__':
    # 在路径中新建文件
    def mkfile(dirname, filename):
        fd = os.path.join(dirname, filename)
        #print(fd)
        if os.path.exists(dirname):
            if not os.path.exists(fd):
                f = open(fd, 'w')
                f.close()
                return 1
        return 0

    #dirname=r'E:\test'
    #if not os.path.exists(dirname):
    #    os.mkdir(dirname)
    #mkfile(dirname,'test1.txt')
    #目录结构:'d:\test(f1(test1.txt,test11.txt),f2(test2.txt),test3.txt)
    print(findFile2(r'D:\test','test'))
    #{'D:\\test': ['test3.txt'], 'D:\\test\\f1': ['test1.txt', 'test11.txt'], 'D:\\test\\f2': ['test2.txt']}