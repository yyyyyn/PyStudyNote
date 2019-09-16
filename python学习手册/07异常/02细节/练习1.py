def getChar(s,i):
    try:
        print(s[i])
    except:
        print('出错')
    else:
        print('else')
        return 'aaa'
    finally:
        print('finally')

if __name__=='__main__':
    print(getChar('abc',1))
    print('==================')
    getChar('abc',4)