a = int(input())
b = int(input())
l = int(input())
N = int(input())
a_trail = (N * 2 - 1) * a
b_trail = ((N-1) * 2) * b
l_free = l * 2
length = a_trail + b_trail + l_free
print(length)
