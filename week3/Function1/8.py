# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    key = [0, 0, 7]
    for i in nums:
        if i == key[0]:
            key.pop(0)
    if len(key) == 0:
        return True
    return False

nums = [int(s) for s in input().split()]
print(spy_game(nums))