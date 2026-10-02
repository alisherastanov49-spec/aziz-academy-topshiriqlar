def par(line):
    key, value = line.split("=")
    return (key, int(value))
def build_dict(pairs):
    d = {}
    for key, value in pairs:
        d[key] = value
    return d
n = int(input())
pairs = []
for _ in range(n):
    pairs.append(par(input()))
print(build_dict(pairs))