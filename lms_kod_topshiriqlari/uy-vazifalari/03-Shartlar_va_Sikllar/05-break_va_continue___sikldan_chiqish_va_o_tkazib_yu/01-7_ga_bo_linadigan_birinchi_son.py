n = int(input())
topildi = False
for i in range(n):
    son = int(input())
    if son % 7 == 0 and not topildi:
        print(son)
        topildi = True
        break
if not topildi:
    print("yo'q")