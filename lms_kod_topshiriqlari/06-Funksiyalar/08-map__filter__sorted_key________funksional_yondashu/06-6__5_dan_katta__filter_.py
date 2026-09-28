sonlar = list(map(int, input().split()))
katta = filter(lambda x: x > 5, sonlar)
print(*katta)