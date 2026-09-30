import math
a, b = map(int, input().split())
g = math.gcd(a, b)
count = 0
for i in range(1, int(math.isqrt(g)) + 1):
    if g % i == 0:
        count += 1
        if i * i != g:
            count += 1
print(count)