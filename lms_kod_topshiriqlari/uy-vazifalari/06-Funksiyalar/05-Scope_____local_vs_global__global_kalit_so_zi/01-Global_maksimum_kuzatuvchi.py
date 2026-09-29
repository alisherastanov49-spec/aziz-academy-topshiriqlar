katta = None
def tekshir(x):
    global katta
    if katta is None or x > katta:
        katta = x
sonlar = list(map(int, input().split()))
katta = sonlar[0]
for x in sonlar:
    tekshir(x)
print(katta)