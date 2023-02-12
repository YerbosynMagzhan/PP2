x = int(input())
y = int(input())
days = 1
z = x
while z < y:
    z = z + z*0.1
    days += 1
print(days)
