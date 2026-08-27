nums = [int(x) for x in input().split()]
copy_nums = nums[:]
copy_nums.sort()
print(*nums)
print(*copy_nums)