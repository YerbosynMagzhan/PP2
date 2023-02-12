a = int(input())
b = 2
while b <= a:
    if a % b == 0:
        print(b)
        break
    b += 1
