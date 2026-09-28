def daraja(n):
    if n == 0:
        return 1
    return 2 * daraja(n - 1)
n = int(input())
print(daraja(n))