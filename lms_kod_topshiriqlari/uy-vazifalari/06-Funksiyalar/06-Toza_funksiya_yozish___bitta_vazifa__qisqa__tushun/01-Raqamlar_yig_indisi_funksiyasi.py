def raqam(n):
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    return yigindi
n = int(input())
print(raqam(n))