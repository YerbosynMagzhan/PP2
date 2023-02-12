el = int(input())
max = 0
while el != 0:
    if max < el:
        max = el
    el = int(input())
print(max)