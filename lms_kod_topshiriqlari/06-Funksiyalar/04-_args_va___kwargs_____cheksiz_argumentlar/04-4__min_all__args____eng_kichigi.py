def min_all(*args):
    return min(args)
nums = list(map(int, input().split()))
print(min_all(*nums))