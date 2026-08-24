n = input().split()
s = 0
for i in range(0, len(n), 2):
    s += int(n[i])
print(s)