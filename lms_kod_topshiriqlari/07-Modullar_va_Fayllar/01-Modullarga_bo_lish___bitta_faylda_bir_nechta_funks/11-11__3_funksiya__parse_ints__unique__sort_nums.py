def par(line):
    return [int(x) for x in line.split()]
def unique(nums):
    return list(set(nums))
def sort(nums):
    return sorted(nums)
nums = sort(unique(par(input())))
print(" ".join(str(x) for x in nums))