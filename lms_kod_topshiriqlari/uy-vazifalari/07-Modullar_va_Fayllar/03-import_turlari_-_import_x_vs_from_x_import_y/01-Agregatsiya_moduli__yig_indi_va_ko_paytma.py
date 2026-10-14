def yigindi(sonlar):
    return sum(sonlar)
def kopaytma(sonlar):
    r = 1
    for x in sonlar:
        r = r * x
    return r
sonlar = [int(x) for x in input().split()]
print(yigindi(sonlar))
print(kopaytma(sonlar))