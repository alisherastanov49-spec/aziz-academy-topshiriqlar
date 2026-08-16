n = int(input())
max_val = int(input())
for _ in range(n - 1):
    num = int(input())
    if num > max_val:
        max_val = num
print(max_val)