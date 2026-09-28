son = list(map(int, input().split()))
tar = sorted(son, reverse=True)
print(*tar)