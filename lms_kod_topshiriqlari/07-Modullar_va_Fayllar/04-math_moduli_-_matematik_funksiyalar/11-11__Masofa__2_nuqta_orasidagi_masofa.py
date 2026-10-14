import math
x, y, x2, y2 = map(float, input().split())
dist = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
print(f"{dist:.2f}")