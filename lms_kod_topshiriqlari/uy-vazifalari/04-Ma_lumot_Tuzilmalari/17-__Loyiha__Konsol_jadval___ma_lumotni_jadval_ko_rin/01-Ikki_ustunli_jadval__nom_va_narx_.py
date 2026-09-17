import sys
data = sys.stdin.read().split()[1:]
for nom, narx in zip(data[::2], data[1::2]):
    print(f"{nom.ljust(10)}{narx.rjust(6)}")