def number(n, rev=0):
    if n == 0:
        return rev
    return number(n // 10, rev * 10 + n % 10)
n = int(input())
print(number(n))