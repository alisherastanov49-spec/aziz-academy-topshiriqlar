import sys
def eng_katta(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
input_data = sys.stdin.read().split()
if len(input_data) >= 3:
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
print(eng_katta(a, b, c))