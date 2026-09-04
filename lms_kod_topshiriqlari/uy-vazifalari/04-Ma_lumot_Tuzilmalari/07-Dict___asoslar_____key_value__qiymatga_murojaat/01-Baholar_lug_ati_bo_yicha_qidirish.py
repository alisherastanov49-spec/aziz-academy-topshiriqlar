n = int(input())
d = {}
for  _ in range(n):
    ism, baho = input().split()
    d[ism] = baho
qidirilyotgan_ism = input()
print(d[qidirilyotgan_ism])