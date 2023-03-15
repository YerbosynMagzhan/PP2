import os

path = '/Users/amirkhamraev/pp2(1)/pp2-22B030460/tsis6/dic-and-files'
os.chdir(path)


result = open('1.txt', 'r')
cnt = 0

for str in result:
    if str != "\n":
        cnt += 1
print(cnt)