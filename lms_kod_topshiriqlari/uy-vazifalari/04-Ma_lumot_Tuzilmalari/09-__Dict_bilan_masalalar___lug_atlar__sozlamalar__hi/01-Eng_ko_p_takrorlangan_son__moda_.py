s = list(map(int, input().split()))
d = {}
for num in s:
    d[num] = d.get(num, 0) + 1
max_count = max(d.values())
candidates = [k for k, v in d.items() if v == max_count]
print(min(candidates))