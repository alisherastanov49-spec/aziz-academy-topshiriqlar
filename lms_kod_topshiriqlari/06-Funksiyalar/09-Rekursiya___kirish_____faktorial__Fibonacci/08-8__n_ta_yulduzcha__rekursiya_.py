def yuz(n):
    if n == 0:
        return ""
    return "*" + yuz(n - 1)
n = int(input())
print(yuz(n))