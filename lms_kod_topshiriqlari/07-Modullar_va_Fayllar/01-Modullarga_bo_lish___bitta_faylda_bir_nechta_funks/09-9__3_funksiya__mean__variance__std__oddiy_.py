import math
def mean(nums):
    return sum(nums) / len(nums)
def v(nums):
    m = mean(nums)
    jami = 0
    for x in nums:
        jami += (x - m) ** 2
    return jami / len(nums)
def std(nums):
    return math.sqrt(v(nums))
nums = list(map(int, input().split()))
print(f"{mean(nums):.2f}")
print(f"{v(nums):.2f}")
print(f"{std(nums):.2f}")