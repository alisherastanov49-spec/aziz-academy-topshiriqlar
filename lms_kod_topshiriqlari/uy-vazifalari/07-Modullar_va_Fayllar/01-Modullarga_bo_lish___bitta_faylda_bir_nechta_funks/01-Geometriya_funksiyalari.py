def yuza(a, b):
    return a * b
def perimetr(a, b):
    return 2 * (a + b)
a, b = [int(x) for x in input().split()]
print(yuza(a, b))
print(perimetr(a, b))