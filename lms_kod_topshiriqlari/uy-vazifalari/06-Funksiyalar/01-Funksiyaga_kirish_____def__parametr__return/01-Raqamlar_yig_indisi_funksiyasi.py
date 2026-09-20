import sys
def raqamlar_yigindisi(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
user_input = sys.stdin.read().strip()
if user_input:
    n = int(user_input)
    print(raqamlar_yigindisi(n))