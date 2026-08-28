numbers = list(map(int, input().split()))
result = [str(x) if x >= 0 else "0" for x in numbers]
print(" ".join(result))