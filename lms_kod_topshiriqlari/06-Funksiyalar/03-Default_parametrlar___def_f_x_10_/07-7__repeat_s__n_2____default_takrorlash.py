import sys
def repeat(s, n=2):
    return s * n
lines = sys.stdin.read().splitlines()
if lines:
    s = lines[0]
    if len(lines) > 1 and lines[1].strip():
        n = int(lines[1].strip())
        print(repeat(s, n))
    else:
        print(repeat(s))