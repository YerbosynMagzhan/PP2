prev = int(input())
cnt = 0
while prev != 0:
    curr = int(input())
    if curr != 0 and curr > prev:
        cnt +=1
    prev = curr
print(cnt)