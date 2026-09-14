n = int(input())
s = {int(input()) for _ in range(n)}
target = int(input())
print(target in s)