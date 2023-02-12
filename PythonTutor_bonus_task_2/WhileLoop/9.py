el = int(input())
max = 0
cnt = 0
knt = 0
while el != 0:
    if max < el:
        max = el
        knt +=1
    cnt += 1
    el = int(input())
print(knt - 1)