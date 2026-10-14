def harf_sanash(soz):
    return len(soz)
def eng_uzun(sozlar):
    eng = sozlar[0]
    for s in sozlar:
        if harf_sanash(s) > harf_sanash(eng):
            eng = s
    return eng
sozlar = input().split()
u = eng_uzun(sozlar)
print(u)
print(harf_sanash(u))