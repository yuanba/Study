#!/usr/bin/python3
import sys

number = sys.argv[1]
filename = sys.argv[2]

target = '../PnD_' + number + '/' + filename

w = open(filename,'w')
r = open(target,'r')
w.write('data;\n')
number = r.readline().strip('\n')
w.write('param n:=' + number + ';\n')
data = r.readline().strip('\n').split()
pdata = []
for i in range(1,len(data)+1):
    pdata.append(str(i))
    pdata.append(data[i-1])
pdata = ' '.join(pdata)
w.write('param w:=' + pdata + ';\n')
print('Transfer the file successfully!')
w.close()
r.close()
    

