sonlar = list(map(int, input().split()))
if sonlar == sorted(sonlar):
    print("Ha")
else:
    print("Yo'q")