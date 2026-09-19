res = [int(x) for x in input().split() if int(x) % 2 == 0 and int(x) % 3 == 0]
print(res)
print(len(res))