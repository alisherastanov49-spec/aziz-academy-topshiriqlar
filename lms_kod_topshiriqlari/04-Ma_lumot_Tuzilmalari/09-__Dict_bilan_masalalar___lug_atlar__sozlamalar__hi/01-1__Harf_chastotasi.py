s = input().strip()
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
result = []
for k, v in d.items():
    result.append(f"{k}:{v}")
print(" ".join(result))