numbers = list(map(int, input().split()))
t = int(input())
result = [str(x) for x in numbers if x > t]
print(" ".join(result))