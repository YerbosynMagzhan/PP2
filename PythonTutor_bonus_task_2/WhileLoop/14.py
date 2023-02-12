# f0 = 0
# f1 = 1
# f2 = f1 + f0
# f3 = f2 + f1
# f4 = f3 + f2
n = int(input())
if n == 0:
    print(0)
else:
    prev, curr = 0, 1
    for i in range(2, n+1):
        prev, curr = curr, prev + curr
print(curr) 