soz = input()
d = {}
for harf in soz:
    if harf in d:
        d[harf] += 1
    else:
        d[harf] = 1
for harf, soni in d.items():
    print(harf, soni)