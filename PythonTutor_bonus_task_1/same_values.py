x = int(input())
y = int(input())
z = int(input())
count = 0
if x == x and x != y and x !=z:
    print(0)
if x == y :
    count +=1
    if x != z:
       count +=1
if x == z:
    count +=1
    if x != y:
       count +=1
if x == y and x == z:
    count +1
print(count)