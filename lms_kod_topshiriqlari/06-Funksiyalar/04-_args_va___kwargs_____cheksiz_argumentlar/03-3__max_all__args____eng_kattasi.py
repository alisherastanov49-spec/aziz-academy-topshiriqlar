def max_all(*args):
    return max(args)
nums = list(map(int, input().split()))
print(max_all(*nums))