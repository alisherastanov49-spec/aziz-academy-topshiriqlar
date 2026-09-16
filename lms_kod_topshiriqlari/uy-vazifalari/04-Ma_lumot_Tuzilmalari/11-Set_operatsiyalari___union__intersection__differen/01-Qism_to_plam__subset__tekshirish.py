a = set(map(int, input().split()))
b = set(map(int, input().split()))
print("Ha" if a.issubset(b) else "Yoq")