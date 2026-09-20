import sys
def ayir(a, b):
    return a - b
data = sys.stdin.read().split()
if len(data) >= 2:
    a = int(data[0])
    b = int(data[1])
    print(ayir(a, b))