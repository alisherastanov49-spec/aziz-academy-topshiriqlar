def power(n):
    if n == 0:
        return 1
    return 3 * power(n - 1)
n = int(input())
print(power(n))