def showFile(fpath):
    block_size=2
    with open('file1.txt','r') as f:
        while True:
            d=f.read(block_size)
            if d:
                yield d
            else:
                return

f=open('file1.txt','w')
f.write('asdfadfwefasdfaef')
f.close()
sf=showFile('file1.txt')
while True:
    print(next(sf))