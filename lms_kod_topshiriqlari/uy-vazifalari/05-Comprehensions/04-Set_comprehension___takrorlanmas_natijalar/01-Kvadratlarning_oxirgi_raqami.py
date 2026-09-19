x = sorted(list({(int(x) ** 2) % 10 for x in input().split()}))
print(x)