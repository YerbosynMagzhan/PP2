def ret(N):
    while N>=0:
        yield N
        N -=1
n = int(input())
#print(*ret(n), ' ')
for i in ret(n):
    print(i)