n = map(int, input().split())
print(*(x * 2 for x in n if x > 0))