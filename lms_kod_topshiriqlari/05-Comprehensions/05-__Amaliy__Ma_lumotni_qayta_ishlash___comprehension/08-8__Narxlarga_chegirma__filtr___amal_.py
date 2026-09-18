narxlar = list(map(int, input().split()))
natija = [p - 10 for p in narxlar if p > 0]
print(natija)