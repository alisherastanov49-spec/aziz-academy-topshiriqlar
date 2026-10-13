def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)
def nok(a, b):
    return a * b // nod(a, b)
a, b = [int(x) for x in input().split()]
print(nok(a, b))