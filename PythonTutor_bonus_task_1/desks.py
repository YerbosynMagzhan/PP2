a = int(input())
b = int(input())
c = int(input())
all = a + b + c
if all % 2 == 1:
    desks = all // 2 + 1
else :
    desks = all // 2
print(desks)