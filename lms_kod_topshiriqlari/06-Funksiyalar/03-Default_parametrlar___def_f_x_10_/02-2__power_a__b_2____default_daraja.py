import sys
def power(a, b=2):
    return a ** b
data = sys.stdin.read().split()
if data:
    if len(data) == 1:
        a = int(data[0])
        print(power(a))
    else:
        a = int(data[0])
        b = int(data[1])
        print(power(a, b))