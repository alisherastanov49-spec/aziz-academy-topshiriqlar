n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split() 
    d[kalit] = qiymat
soralgan_kalit = input()
print(d[soralgan_kalit])