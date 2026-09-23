def avg_all(*args):
    if not args:
        return 0.0
    return sum(args) / len(args)
nums = list(map(int, input().split()))
print(f"{avg_all(*nums):.2f}")