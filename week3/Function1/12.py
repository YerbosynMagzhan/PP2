def histogram(nums):
    for i in nums:
        print("*"*i)
nums = [int(i) for i in input().split()]
histogram(nums)