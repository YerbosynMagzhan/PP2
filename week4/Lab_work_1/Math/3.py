import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
area = (pow(a, 2) * n) / (4 * math.tan(180/n))
print(area) 