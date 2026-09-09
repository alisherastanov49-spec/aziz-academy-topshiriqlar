n = int(input())
d = {}
for _ in range(n):
    word = input().strip()
    d[word] = d.get(word, 0) + 1
izlanadigan = input().strip()
print(d.get(izlanadigan, 0))