'''
将数据保存到csv文件中，可以使用内置的csv模块
'''
import csv

csvFile1=open("test.csv",'w+')
try:
    writer=csv.writer(csvFile1)
    writer.writerow(('number','number plus 2','number times 3'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile1.close()