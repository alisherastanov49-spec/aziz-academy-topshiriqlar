n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)
best_name, best_score = max(d.items(), key=lambda x: (x[1], -ord(x[0][0])))
print(f"{best_name} {best_score}")