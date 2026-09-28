def tes(n):
    if n == 1:
        return [1]
    return [n] + tes(n - 1)
n = int(input())
print(*tes(n))