import os
f1=open("tsis6/dic-and-files/1.txt", "r")
f2=open("tsis6/dic-and-files/2.txt", "w")
for line in f1:
    f2.write(line)