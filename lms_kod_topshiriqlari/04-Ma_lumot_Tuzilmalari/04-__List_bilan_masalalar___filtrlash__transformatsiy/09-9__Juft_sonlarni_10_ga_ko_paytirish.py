n = input()
nums = [int(x) for x in input().split()]
result = [x * 10 for x in nums if x % 2 == 0]
print(result)