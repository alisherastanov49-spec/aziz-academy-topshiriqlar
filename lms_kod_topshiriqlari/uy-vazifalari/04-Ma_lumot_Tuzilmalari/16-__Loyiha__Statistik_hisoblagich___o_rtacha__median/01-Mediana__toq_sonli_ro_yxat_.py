import sys 
nums = list(map(int, sys.stdin.read().split()))
if nums:
    nums.sort()
    print(nums[len(nums) // 2])