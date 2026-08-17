import sys
data = sys.stdin.read().split()
res, i = 0, 0
while data[i] != '=':
    op, num = data[i], int(data[i+1])
    if op == '+': res += num
    elif op == '-': res -= num
    elif op == '*': res *= num
    elif op == '/' and num: res //= num
    i += 2
print(res)