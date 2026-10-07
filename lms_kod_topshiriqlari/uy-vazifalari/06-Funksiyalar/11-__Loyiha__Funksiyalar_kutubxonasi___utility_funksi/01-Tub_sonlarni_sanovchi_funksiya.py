a, b = map(int, input().split())
n = 0
for x in range(a, b + 1):
    if x > 1 and all(x % i for i in range(2, x)):
        n += 1
print(n)