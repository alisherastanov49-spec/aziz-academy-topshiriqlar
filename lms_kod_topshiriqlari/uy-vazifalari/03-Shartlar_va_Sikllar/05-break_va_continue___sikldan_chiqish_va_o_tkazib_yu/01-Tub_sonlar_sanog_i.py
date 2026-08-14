s = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        s += 1
print(s)