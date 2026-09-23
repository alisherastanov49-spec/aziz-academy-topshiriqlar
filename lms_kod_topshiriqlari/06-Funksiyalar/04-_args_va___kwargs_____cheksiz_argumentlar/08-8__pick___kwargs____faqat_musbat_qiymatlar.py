def pick(**kwargs):
    return {k: v for k, v in kwargs.items() if v > 0}

n = int(input())
data = {}
for _ in range(n):
    line = input().split()
    key = line[0]
    value = int(line[1])
    data[key] = value 

print(pick(**data))