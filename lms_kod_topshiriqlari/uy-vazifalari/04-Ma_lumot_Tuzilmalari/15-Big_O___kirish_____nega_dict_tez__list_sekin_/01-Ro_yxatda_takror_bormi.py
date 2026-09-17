import sys
items = sys.stdin.read().split()
if len(items) != len(set(items)):
    print("Ha")
else:
    print("Yoq")