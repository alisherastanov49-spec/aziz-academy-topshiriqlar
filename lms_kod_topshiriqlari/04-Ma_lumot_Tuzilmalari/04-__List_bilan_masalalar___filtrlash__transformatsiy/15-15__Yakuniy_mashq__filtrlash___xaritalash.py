n = input()
nums = [int(x) for x in input().split()]
result = [x * 2 for x in nums if x > 0]
print(result)