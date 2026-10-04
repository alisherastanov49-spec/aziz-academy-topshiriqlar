n = list(map(int, input().split()))
result = [x * x for x in n if x % 2 == 0]
result.reverse()
print(*result)