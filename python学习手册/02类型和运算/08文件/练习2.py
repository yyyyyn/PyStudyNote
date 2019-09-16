'''
将数据进行二进制打包存储在文件中个，再解析
'''

import pickle
import struct

f=open(r'testfile/test2.pkl','wb')
data=struct.pack('i4sh',7,b'abcd',8)
pickle.dump(data,f)
f.close()

f=open(r'testfile/test2.pkl','rb')
data=pickle.load(f)
D=struct.unpack('i4sh',data)
print(D)
f.close()