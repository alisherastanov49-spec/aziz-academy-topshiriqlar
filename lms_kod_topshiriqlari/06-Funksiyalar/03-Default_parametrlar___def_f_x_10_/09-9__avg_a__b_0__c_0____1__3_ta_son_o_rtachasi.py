import sys
def avg(*args):
    return sum(args) / len(args)
data = [float(i) for i in sys.stdin.read().split()]
if data:
    result = avg(*data)
    print(f"{result:.2f}")