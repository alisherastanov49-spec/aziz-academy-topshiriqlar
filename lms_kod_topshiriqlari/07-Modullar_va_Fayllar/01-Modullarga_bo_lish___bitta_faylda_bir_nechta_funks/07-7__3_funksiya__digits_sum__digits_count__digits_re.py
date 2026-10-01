
def dig(s):
    return sum(int(d) for d in str(n))
def digt(n):
    return len(str(n))
def digts(n):
    return int(str(n)[::-1])
s = input().strip()
n = int(s)
print(dig(n))
print(digt(n))
print(digts(n))