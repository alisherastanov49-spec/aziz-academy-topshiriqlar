def yigindi(n):
    if n <= 1:
        return n
    return n + yigindi(n - 1)
n = int(input())
print(yigindi(n))