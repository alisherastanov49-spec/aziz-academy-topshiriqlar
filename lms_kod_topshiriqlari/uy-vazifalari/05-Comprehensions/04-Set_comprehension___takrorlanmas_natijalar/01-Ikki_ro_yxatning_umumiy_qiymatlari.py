a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(sorted(list({x for x in a if x in b})))