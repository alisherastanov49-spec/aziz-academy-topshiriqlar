n = input()
nums = [int(x) for x in input().split()]
result = [x for x in nums if 0 < x < 100]
print(result)