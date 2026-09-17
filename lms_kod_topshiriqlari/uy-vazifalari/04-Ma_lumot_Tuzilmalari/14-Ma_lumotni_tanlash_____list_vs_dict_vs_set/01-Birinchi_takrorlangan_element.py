import sys
items = sys.stdin.read().split()
seen = set()
for item in items:
    if item in seen:
        print(item)
        break
    seen.add(item)
else:
    print("yoq")