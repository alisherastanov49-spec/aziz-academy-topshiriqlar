n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = d.get(k, 0) + int(v)
for k in sorted(d):
    print(f"{k} {d[k]}")