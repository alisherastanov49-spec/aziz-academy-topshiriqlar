sonlar = list(map(int, input().split()))
natija = [x * x for x in sonlar if x % 2 == 0]
print(natija)