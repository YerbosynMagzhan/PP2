def evennum(N):
    nums = 0 
    while True:
        if (nums % 2) == 0:
            yield nums
        if nums==N:
            break
        else : nums+=1
        
n = int(input())
print(*evennum(n), ' ')