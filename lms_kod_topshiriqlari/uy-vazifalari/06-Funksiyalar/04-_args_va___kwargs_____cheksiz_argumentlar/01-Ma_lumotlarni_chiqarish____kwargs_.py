def malumot(**kwargs):
    res = []
    for k, v in kwargs.items():
        res.append(f"{k}: {v}")
    return res
n = int(input())
d = {}
for _ in range(n):
    k, v = input().split('=')
    d[k] = v
for i in malumot(**d):
    print(i)