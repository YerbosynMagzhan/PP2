def div(N):
    x  = 0
    while True:
        if (x % 3 == 0) and (x % 4 ==0):
            yield x
        if x == N:
            break
        else: x+=1
            
n = int(input())
print(*div(n), ' ')