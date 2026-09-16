n = int(input())
oquvchilar = []
for _ in range(n):
    ism, baho = input().split()
    oquvchilar.append({"ism": ism, "baho": int(baho)})
ortacha = sum(o["baho"] for o in oquvchilar) / n
for o in oquvchilar:
    if o["baho"] > ortacha:
        print(o["ism"])