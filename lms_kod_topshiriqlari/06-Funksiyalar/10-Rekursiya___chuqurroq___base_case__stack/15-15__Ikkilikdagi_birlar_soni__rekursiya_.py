def one(n):
    if n == 0:
        return 0
    return (n % 2) + one(n // 2)
n = int(input())
print(one(n))