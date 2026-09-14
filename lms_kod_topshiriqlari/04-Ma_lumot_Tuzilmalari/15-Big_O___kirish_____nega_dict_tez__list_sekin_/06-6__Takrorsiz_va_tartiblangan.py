sonlar = map(int, input().split())
unikal_tartiblangan = sorted(set(sonlar))
print(*unikal_tartiblangan)