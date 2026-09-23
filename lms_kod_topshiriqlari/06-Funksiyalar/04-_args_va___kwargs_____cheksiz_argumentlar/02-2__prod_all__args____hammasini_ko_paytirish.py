import math
def prod_all(*args):
    return math.prod(args)
nums = list(map(int, input().split()))
print(prod_all(*nums))