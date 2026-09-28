def squer(n):
    if n <= 1:
        return 1
    return n**2 + squer(n - 1)
n = int(input())
print(squer(n))