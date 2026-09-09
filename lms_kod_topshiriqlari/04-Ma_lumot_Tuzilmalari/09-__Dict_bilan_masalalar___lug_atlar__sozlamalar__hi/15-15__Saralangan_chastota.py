s = input().strip()
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
for k in sorted(d):
    print(f"{k}={d[k]}")