def savat(*narxlar, chegirma=0):
    jami = sum(narxlar)
    return jami - jami * chegirma // 100
narxlar = list(map(int, input().split()))
chegirma = int(input())
natija = savat(*narxlar, chegirma=chegirma)
print(natija)