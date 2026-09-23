def sum_all(*args):
    return sum(args)
nums = list(map(int, input().split()))
print(sum_all(*nums))