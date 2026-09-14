numbers = input().split()
seen = set()
dups = set()
for num in numbers:
    if num in seen:
        dups.add(num)
    else:
        seen.add(num)
print(len(dups))