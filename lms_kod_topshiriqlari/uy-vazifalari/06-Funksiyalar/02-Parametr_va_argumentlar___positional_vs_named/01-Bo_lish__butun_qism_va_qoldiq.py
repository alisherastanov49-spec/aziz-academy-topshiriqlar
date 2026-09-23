def bol(a, b):
    butun = a // b
    qoldiq = a % b
    return f"{butun} {qoldiq}"
a = int(input())
b = int(input())
print(bol(a, b))