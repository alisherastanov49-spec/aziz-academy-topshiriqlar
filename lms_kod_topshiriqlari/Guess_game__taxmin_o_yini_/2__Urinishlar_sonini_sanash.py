secret = 7
urinishlar = 0
print("Men 1 dan 10 gacha bo'lgan sonni o'yladim. Topishga harakat qiling!")
while True:
    try:
        taxmin = int(input())
        urinishlar += 1
        if taxmin < secret:
            print("Kichik")
        elif taxmin > secret:
            print("Katta")
        else:
            print(f"To'g'ri! Siz {urinishlar} ta urinishda topdingiz.")
            break
        except ValueError:
            print("Iltimos, faqat son kiriting!")