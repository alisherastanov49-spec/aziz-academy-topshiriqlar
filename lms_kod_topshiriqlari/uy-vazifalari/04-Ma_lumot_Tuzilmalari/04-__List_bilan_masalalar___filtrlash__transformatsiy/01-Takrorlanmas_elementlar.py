items = input().split()
seen = []
for item in items:
    if item not in seen:
        seen.append(item)
print(" ".join(seen))