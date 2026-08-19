start = int(input())
step = int(input())
if step <= 0 or start >= 100:
    if start >= 100:
        print(0)
    else:
        print("CHEKSIZ")
else:
    qadamlar = 0
    while start < 100:
        start += step
        qadamlar += 1
    print(qadamlar)