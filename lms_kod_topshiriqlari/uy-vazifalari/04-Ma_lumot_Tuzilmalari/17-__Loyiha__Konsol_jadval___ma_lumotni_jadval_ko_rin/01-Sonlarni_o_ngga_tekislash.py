import sys
for x in sys.stdin.read().split()[1:]:
    print(x.rjust(6))