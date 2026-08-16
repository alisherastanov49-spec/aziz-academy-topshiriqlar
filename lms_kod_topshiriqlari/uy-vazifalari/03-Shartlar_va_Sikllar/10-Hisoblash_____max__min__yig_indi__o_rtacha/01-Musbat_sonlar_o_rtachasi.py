n = int(input())
total_sum = 0
count = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        total_sum += num
        count += 1
if count > 0:
    print(total_sum // count)
else:
    print(0)