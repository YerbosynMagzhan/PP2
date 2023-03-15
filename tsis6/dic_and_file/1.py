# k = open('tsis6/1.txt','r')
# print(k.read())

# import os
# #f_path =r'\\Users\\amirkhamraev\\pp2(1)\\pp2-22B030460\\tsis6\\dic-and-files\\1.py'
# puti = os.getcwd()
# p = os.listdir(puti)
# print(p)

import os
b = os.getcwd()
a = os.listdir(b)
print('All dic:')
for i in a:
    if os.path.isdir(i):
        print (i)
print('all files and dic:')
for i in a:    
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
print('all files:')
for i in a:
    if os.path.isfile(i):
        print(i)