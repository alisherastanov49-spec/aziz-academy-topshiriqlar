soat = int(input())
soatlik_narxi = int(input())
soliq_foizi = int(input())
yalpi = soat * soatlik_narxi 
soliq = yalpi * soliq_foizi // 100
aniq = yalpi - soliq
print(yalpi)
print(soliq)
print(aniq)
