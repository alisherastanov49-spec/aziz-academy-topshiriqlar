ism = input()
ballar = list(map(int, input().split()))
d = {ism: ballar}
print(sum(d[ism]))