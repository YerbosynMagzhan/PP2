import os

path = r'/Users/amirkhamraev/pp2(1)/pp2-22B030460'
os.chdir(path)

for i in range(65, 91):
    res = open(chr(i)+'.txt', 'w') 