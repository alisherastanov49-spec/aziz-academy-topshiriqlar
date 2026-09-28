son = list(map(int, input().split()))
man = filter(lambda x: x < 0, son)
print(*man)