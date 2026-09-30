a, b = map(int, input().split())
def prime(n):
    if n < 2:
        return False
    for  i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
count = sum(1 for x in range(a, b + 1) if prime(x))
print(count)