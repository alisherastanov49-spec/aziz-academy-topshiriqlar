def l(lst):
    if not lst:
        return 0
    return lst[0] + l(lst[1:])
numbers = list(map(int, input().split()))
print(l(numbers))