n = int(input())
d = {}
for _ in range(n):
    name, price = input().split()
    d[name] = price
search_key = input().strip()
print(d.get(search_key, "Topilmadi"))