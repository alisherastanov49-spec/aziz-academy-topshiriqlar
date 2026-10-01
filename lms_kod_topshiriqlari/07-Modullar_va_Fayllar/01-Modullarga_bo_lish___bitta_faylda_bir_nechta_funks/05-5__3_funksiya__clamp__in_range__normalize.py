x, low, high = map(float, input().split())
def clamp(v, l, h): return max(l, min(v, h))
def ran(v, l, h): return l <= v <= h
def nor(v, l, h): return (v - l) / (h - l)
c = clamp(x, low, high)
print(int(c) if c.is_integer() else c)
print(ran(x, low, high))
print(f"{nor(x, low, high):.2f}")