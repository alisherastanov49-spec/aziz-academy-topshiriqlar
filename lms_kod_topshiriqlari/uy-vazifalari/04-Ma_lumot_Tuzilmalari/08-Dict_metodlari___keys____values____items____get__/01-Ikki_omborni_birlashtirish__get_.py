total = {}
n = int(input())
for _ in range(n):
    name, qyt = input().split()
    total[name] = total.get(name, 0) + int(qyt)
    
m = int(input())
for _ in range(m):
    name, qty = input().split()
    total[name] = total.get(name, 0) + int(qty)
for name in sorted(total):
    print(name, total[name])
    