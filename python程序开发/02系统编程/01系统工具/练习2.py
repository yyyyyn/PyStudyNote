#一个自定义分页的脚本
def more(text,numlines=15):
    lines=text.splitlines()
    while lines:
        chunk=lines[:numlines]
        lines=lines[numlines:]
        for l in chunk:print(l)
        if lines and input('More?') not in ['y','Y']:break


def more1(text,numlines=8):
    "限定文本显示每行字数，打印出来"
    lines=text.splitlines()
    for l in lines:
        if len(l)<=numlines:
            print(l)
            continue
        while l:
            if len(l) <= numlines:
                print(l)
                break
            print(l[:numlines])
            l=l[numlines:]
def more2(text,numlines=10):
    print(len(text))

    while True:
        if len(text)<=numlines:
            print(text)
            break
        print(text[:numlines])
        text=text[numlines:]

if __name__=='__main__':
    #for l in open('知识点.txt',mode='r',encoding='UTF-8'):
    #    print(l)
    #print(open('知识点.txt',mode='r',encoding='UTF-8').read().splitlines())
    more(open('知识点.txt',mode='r',encoding='UTF-8').read(),2)

