import sys
for x in sys.stdin.read().split()[1:]:
    print(f"{x.ljust(12)}|")