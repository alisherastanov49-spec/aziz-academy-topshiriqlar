import sys
def slice_text(s, start=0, end=None):
    if end is None:
        return s[start:]
    return s[start:end]
lines = sys.stdin.read().split()
if lines:
    s = lines[0]
    start = int(lines[1]) if len(lines) > 1 else 0
    end = int(lines[2]) if len(lines) > 2 else None
    print(slice_text(s, start, end))