import sys
nums = list(map(int, sys.stdin.read().split()))
if nums:
    print(max(nums) - min(nums))