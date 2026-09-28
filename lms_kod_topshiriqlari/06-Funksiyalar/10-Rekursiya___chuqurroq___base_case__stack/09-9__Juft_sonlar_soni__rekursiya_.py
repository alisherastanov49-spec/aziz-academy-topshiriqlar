def even(lst):
    if not lst:
        return 0
    is_even = 1 if lst[0] % 2 == 0 else 0
    return is_even + even(lst[1:])
numbers = list(map(int, input().split()))
print(even(numbers))