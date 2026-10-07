def fmt(key, values):
    return key + "=" + values
def fmt_table(a, b, c):
    return a + " | " + b + " | " + c
key = input()
value = input()
a, b, c = input().split()
print(fmt(key, value))
print(fmt_table(a, b, c))