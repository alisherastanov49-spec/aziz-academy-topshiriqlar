def raq(n):
    if n < 10:
        return n
    return (n % 10) + raq(n // 10)
n = int(input())
print(raq(n))