import sys
data = list(map(int, sys.stdin.read().split()))
R, i, res = data[0], 1, []
for r in range(1, R + 1):
    secret, attempts = data[i], 0
    i += 1
    while True:
        attempts += 1
        if data[i] == secret:
            i += 1
            break
        i += 1
    res.append(attempts)
    print(f"Round {r}: {attempts} urinish")
print(f"Jami: {sum(res)}\nEng yaxshi: {min(res)}")