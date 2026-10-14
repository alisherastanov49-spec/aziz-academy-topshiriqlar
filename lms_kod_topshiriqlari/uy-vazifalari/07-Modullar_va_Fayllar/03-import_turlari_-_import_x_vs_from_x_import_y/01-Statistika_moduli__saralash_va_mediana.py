def saralash(sonlar):
    return sorted(sonlar)
def mediana(sonlar):
    s = sorted(sonlar)
    n = len(s)
    o = n // 2
    if n % 2 == 1:
        return s[o]
    return (s[o - 1] + s[o]) / 2
sonlar = [int(x) for x in input().split()]
print(" ".join(str(x) for x in saralash(sonlar)))
print(mediana(sonlar))