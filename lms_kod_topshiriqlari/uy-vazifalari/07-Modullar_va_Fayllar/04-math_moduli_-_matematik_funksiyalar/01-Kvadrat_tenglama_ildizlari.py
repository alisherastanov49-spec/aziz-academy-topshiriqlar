import math
a, b, c = map(int, input().split())
d = b * b - 4 * a * c
if d < 0:
    print("Haqiqiy ildiz yo'q")
elif d == 0:
    print(round(-b / (2 * a), 2))
else:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(round(min(x1, x2), 2), round(max(x1, x2),2))