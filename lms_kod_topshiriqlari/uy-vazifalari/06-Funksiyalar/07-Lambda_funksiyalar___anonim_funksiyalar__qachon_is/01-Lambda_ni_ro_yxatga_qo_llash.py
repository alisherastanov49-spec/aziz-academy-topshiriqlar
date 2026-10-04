nums = map(int, input().split())
print(*(x * x + 1 for x in nums))