n = int(input())

sum = 0
for i in range(1, n+1):
    sum += i
for j in range(n-1):
    number = int(input())
    sum -= number
print(sum)