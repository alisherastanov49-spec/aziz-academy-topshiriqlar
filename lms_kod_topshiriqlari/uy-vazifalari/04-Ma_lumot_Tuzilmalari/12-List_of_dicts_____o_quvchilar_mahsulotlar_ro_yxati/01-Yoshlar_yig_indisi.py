n = int(input())
oquvchilar = []
for _ in range(n):
    ism, yosh = input().split()
    oquvchilar.append({"ism": ism, "yosh": int(yosh)})
print(sum(o["yosh"] for o in oquvchilar))