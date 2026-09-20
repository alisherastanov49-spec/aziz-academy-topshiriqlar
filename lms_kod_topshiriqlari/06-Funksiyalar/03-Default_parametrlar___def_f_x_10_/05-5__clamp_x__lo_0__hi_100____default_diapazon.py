import sys
def clamp(x, lo=0, hi=100):
    return max(lo, min(x, hi))
data = [int(i) for i in sys.stdin.read().split()]
if data:
    if len(data) == 1:
        print(clamp(data[0]))
    elif len(data) == 2:
        print(clamp(data[0], data[1]))
    else:
        print(clamp(data[0], data[1], data[2]))