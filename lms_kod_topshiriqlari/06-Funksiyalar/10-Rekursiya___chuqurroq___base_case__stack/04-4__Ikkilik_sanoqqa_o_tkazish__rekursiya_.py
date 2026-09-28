def bin(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return bin(n // 2) + str(n % 2)
n = int(input())
print(bin(n))