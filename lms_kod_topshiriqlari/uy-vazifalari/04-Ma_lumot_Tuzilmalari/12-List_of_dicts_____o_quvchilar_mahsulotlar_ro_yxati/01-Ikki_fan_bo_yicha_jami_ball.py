n = int(input())
oquvchilar = []
for _ in range(n):
    ism, mat, fiz = input().split()
    oquvchilar.append({"ism": ism, "mat": int(mat), "fiz": int(fiz)})
for o in oquvchilar:
    print(o["ism"], o["mat"] + o["fiz"])