import sys
data = sys.stdin.read().split()
d = dict(zip(data[1:-1:2], data[2:-1:2]))
print(d.get(data[-1], "Yo'q"))