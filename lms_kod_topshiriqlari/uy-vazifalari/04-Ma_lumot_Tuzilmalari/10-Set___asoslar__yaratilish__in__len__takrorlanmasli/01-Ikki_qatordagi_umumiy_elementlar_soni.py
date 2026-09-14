set1 = set(input().split())
set2 = set(input().split())
count = 0
for x in set1:
    if x in set2:
        count += 1
print(count)