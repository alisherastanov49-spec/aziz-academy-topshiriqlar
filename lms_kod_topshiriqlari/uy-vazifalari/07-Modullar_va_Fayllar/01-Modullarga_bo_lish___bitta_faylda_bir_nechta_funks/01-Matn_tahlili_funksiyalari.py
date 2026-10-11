def unli_sanash(s):
    unlilar = "aeiou"
    c = 0
    for ch in s:
        if ch in unlilar:
            c = c + 1
    return c
def soz_sanash(s):
    return len(s.split())
s = input()
print(unli_sanash(s))
print(soz_sanash(s))