def kub(x):
    return x * x * x
def yig(n):
    return sum(kub(i) for i in range(1, n + 1))
n = int(input())
print(yig(n))