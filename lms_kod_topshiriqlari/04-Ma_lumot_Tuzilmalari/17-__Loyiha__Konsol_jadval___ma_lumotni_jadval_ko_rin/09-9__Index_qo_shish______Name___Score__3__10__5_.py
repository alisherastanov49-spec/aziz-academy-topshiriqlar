n = int(input())
for i in range(1, n + 1):
    qator = input().strip()
    ism, ball = qator.split()
    print(f"{i}|{ism}|{ball}")