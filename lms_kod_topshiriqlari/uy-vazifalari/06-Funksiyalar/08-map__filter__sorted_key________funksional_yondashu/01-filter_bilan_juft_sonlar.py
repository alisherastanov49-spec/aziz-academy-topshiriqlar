n = map(int, input().split())
print(*(x for x in n if x % 2 == 0))