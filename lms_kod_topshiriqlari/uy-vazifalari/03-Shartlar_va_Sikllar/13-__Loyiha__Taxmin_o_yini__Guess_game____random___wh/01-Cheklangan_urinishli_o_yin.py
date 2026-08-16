import sys
secret, n, *guesses = map(int, sys.stdin.read().split())
for g in guesses[:n]:
    if g == secret:
        print("TOPDINGIZ")
        break
    print("KATTA" if g > secret else "KICHIK")
else:
    print("YUTQAZDINGIZ")