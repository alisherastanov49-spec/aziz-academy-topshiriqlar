sonlar = list(map(int, input().split()))
toqlar = filter(lambda x: x % 2 != 0, sonlar)
print(*toqlar)