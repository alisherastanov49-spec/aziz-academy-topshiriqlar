def kabisa(yil):
    return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)
def kunlar(oy, yil):
    if oy in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if oy in (4, 6, 9, 11):
        return 30
    if kabisa(yil):
        return 29
    return 28
oy, yil = [int(x) for x in input().split()]
print(kunlar(oy, yil))
