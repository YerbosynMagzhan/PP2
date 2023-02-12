n = int(input())
cnt = 1
if n == 0:
    print(cnt)
prev, curr = 0, 1
while curr <=n:
    if curr == n:
        print(cnt)
        break
    prev, curr = curr, prev + curr
    cnt += 1
else: print(-1)
        