n = int(input())
d = {}
for _ in range(n):
    name, price = input().split()
    d[name] = int(price)
print(sum(d.values()))