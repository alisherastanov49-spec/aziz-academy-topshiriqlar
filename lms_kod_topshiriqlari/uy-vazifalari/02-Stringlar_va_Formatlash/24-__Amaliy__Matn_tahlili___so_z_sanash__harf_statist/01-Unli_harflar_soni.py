s = input().lower()
soni = 0
for harf in "aeiou":
    soni += s.count(harf)
print(soni)