def juftlar(sonlar):
    return [x for x in sonlar if x % 2 == 0]
def toqlar(sonlar):
    return [x for x in sonlar if x % 2 != 0]
sonlar = [int(x) for x in input().split()]
print(" ".join(str(x) for x in juftlar(sonlar)))
print(" ".join(str(x) for x in toqlar(sonlar)))