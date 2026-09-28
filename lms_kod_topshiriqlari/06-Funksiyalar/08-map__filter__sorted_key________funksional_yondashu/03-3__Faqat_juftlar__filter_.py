sonlar = list(map(int, input().split()))
juftlar = filter(lambda x: x % 2 == 0, sonlar)
print(*juftlar)