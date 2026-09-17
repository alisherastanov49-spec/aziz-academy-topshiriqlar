import sys
data = sys.stdin.read().split()[1:]
a = sorted([(-int(bal), ism) for ism, bal in zip(data[::2], data[1::2])])
for bal, ism in a:
    print(ism, -bal)