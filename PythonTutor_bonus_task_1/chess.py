a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 == 1 and b % 2 == 1:
    color1 = "black"
elif a % 2 == 0 and b % 2 == 0:
    color1 = "black"
else: color1 = "white"

if c % 2 == 1 and d % 2 == 1:
    color2 = "black"
elif c % 2 == 0 and d % 2 == 0:
    color2 = "black"
else: color2 = "white"

if color1 == color2:
    print("YES")
else: print("NO")