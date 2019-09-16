class MyException(Exception):
#自定义异常类
    def showMessage(self):
        print('错误，因为我讨厌字母p!')

def getChar(s='spam',i=0):
    try:
        if s[i]=='p':
            raise MyException() #手动抛出异常
        assert s[i]!='a','我讨厌字母a'
        #表达式结果为False则抛出AssertionError异常
        return s[i]
    except MyException as e:
        e.showMessage()
    except AssertionError as e:
        print(e)
        #打印手动抛出异常结果
        return  'aaa'
    except IndexError:
        print('索引异常!')
    except:
        print('其它异常!')
    finally:
        print('finally')

if __name__=='__main__':
    print(getChar('spam',2))

