def genf(N):
    x = 1
    while x<=N:
        yield x**2
        x+=1
        
n = int(input())
for x in genf(n):
    print(x)