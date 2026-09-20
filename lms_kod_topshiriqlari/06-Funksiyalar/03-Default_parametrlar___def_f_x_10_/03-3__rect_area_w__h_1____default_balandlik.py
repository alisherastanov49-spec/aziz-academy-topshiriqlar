import sys
def rect_area(w, h=1):
    return w * h
data = sys.stdin.read().split()
if data:
    if len(data) == 1:
        w = int(data[0])
        print(rect_area(w))
    else:
        w = int(data[0])
        h = int(data[1])
        print(rect_area(w, h))