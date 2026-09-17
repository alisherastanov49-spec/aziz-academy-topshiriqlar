import sys
nums = list(map(int, sys.stdin.read().split()))
if nums:
    avg = sum(nums) / len(nums)
    print(round(avg, 2))