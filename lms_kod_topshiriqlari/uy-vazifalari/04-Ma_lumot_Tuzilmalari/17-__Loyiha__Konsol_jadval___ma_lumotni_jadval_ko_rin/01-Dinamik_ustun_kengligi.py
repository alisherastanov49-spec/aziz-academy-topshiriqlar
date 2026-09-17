import sys
names = sys.stdin.read().split()[1:]
if names:
    w = max(len(x) for x in names)
    for x in names:
        print(f"{x.ljust(w)}|")
        