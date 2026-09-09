n = int(input())
max_key = None
max_val = float('-inf')
for _ in range(n):
    k, v = input().split()
    v = int(v)
    if v > max_val:
        max_val = v
        max_key = k
print(max_key)