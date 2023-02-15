# def has_33(nums):
#     pass

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(ints):
    for i in range(len(ints)-1):
        if ints[i] == 3 and ints[i+1] == 3:
            return True
    return False

ints = [int(s) for s in input().split()]
print(has_33(ints))