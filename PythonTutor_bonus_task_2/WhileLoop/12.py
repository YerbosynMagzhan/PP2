max = int(input())
smax = int(input())
if max < smax:
    max, smax = smax, max
el = int(input())
while el != 0:
    if max < el:
        max, smax = el, max
    elif smax < el:
        smax = el
    el = int(input())
print(smax)

