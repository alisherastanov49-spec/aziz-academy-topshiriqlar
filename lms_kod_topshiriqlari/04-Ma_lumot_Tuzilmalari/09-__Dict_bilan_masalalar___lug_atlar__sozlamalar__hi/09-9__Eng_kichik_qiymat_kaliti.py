n = int(input())
min_key = None
min_val = float('inf')
for _ in range(n):
    k, v = input().split()
    v = int(v)
    if v < min_val:
        min_val = v
        min_key = k
print(min_key)