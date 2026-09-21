import sys
def tax(price, rate=12):
    return price + (price * rate / 100)
args = sys.stdin.read().split()
if len(args) == 1:
    print(f"{tax(float(args[0])):.2f}")
elif len(args) >= 2:
    print(f"{tax(float(args[0]), float(args[1])):.2f}")