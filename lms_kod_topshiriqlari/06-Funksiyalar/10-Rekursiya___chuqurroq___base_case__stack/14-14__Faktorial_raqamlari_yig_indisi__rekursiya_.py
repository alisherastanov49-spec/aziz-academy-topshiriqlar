def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)
def dig(n):
    if n == 0:
        return 0
    return (n % 10) + dig(n // 10)
n = int(input())
fact = fac(n)
print(dig(fact))