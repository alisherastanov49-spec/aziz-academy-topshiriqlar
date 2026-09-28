sonlar = list(map(int, input().split()))
kvadratlar = map(lambda x: x**2, sonlar)
print(*kvadratlar)