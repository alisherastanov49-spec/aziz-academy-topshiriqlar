jami_sekund = int(input().strip())
soat = jami_sekund // 3600
qolgan = jami_sekund % 3600
minut = qolgan // 60
soniya = qolgan % 60
print(soat)
print(minut)
print(soniya)