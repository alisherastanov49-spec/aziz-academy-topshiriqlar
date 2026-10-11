def eng_katta(sonlar):
    return max(sonlar)
def eng_kichik(sonlar):
    return min(sonlar)
def diapazon(sonlar):
    return eng_katta(sonlar) - eng_kichik(sonlar)
sonlar = [int(x) for x in input().split()]
print(eng_katta(sonlar))
print(eng_kichik(sonlar))
print(diapazon(sonlar))