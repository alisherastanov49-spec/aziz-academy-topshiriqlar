a = set(input().split())
b = set(input().split())
natija = sorted(a - b)
print(*natija)