n = int(input())
d = {}
for _ in range(n):
    nom, miqdor = input().split()
    miqdor = int(miqdor)
    if nom in d:
        d[nom] += miqdor
    else:
        d[nom] = miqdor
for nom, miqdor in d.items():
    print(nom, miqdor)