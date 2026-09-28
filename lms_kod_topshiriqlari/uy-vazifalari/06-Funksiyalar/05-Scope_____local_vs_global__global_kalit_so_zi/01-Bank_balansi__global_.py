balans = 0
def kirim(x):
    global balans
    balans += x
def chiqim(x):
    global balans
    balans -= x
n = int(input())
for _ in range(n):
    amal = input()
    if amal[0] == '+':
        kirim(int(amal[1:]))
    else:
        chiqim(int(amal[1:]))
print(balans)