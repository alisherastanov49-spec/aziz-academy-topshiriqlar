son = list(map(int, input().split()))
mus = list(filter(lambda x: x > 0, son))
print(len(mus))