def yigindi(oxir, boshlanish=1):
    return sum(range(boshlanish, oxir + 1))
oxir = int(input())
boshlanish = int(input())
print(yigindi(oxir))
print(yigindi(oxir, boshlanish))