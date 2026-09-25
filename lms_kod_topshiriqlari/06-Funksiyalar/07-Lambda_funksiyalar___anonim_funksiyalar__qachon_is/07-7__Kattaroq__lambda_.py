a, b = map(int, input().split())
kattaroq = lambda x, y: x if x > y else y
print(kattaroq(a, b))