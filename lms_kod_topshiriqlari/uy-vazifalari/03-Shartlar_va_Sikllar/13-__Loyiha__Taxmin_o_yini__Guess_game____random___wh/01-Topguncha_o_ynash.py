import sys
secret, * guesses = map(int, sys.stdin.read().split())
for i, guess in enumerate(guesses, 1):
    if guess == secret:
        print(f"TOPDINGIZ\nUrinishlar: {i}")
        break
    print("KATTA" if guess > secret else "KICHIK")