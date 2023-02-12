el = -1
max = 0
cnt = 1
while el != 0:
    el = int(input())
    if max < el:
        max = el
    elif max == el:
        cnt +=1
print(cnt)
