def cel(f):
    return (f - 32) * 5 / 9
def fah(c):
    return (c * 9 / 5) + 32
unit = input().strip()
val = float(input().strip())
if unit == 'C':
    print(f"{cel(val):.2f}")
elif unit == 'F':
    print(f"{fah(val):.2f}")