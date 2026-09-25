def jadval(son, nechtagacha=5):
    natija = [str(son * i) for i in range(1, nechtagacha + 1)]
    return " ".join(natija)
son = int(input())
nechtagacha = int(input())
print(jadval(son))
print(jadval(son, nechtagacha))