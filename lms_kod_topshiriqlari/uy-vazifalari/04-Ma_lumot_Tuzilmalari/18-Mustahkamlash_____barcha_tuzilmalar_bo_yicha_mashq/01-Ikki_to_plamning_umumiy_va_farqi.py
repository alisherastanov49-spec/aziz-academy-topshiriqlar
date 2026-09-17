import sys
a, b = [set(map(int, line.split())) for line in sys.stdin.read().splitlines()]
print(*sorted(a & b))
print(*sorted(a - b))