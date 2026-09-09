n = int(input())
d = {}
for _ in range(n):
    word = input().strip()
    d[word] = 1
print(len(d))