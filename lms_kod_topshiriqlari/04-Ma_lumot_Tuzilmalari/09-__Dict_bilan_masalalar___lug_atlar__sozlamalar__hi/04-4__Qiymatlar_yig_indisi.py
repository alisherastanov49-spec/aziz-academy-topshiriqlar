n = int(input())
d = {}
for i in range(n):
    d[f"k{i}"] = int(input())
print(sum(d.values()))