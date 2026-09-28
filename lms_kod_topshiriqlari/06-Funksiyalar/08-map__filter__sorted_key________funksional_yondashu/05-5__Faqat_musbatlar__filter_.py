sonlar = list(map(int, input().split()))
musbatlar = filter(lambda x: x > 0, sonlar)
print(*musbatlar)