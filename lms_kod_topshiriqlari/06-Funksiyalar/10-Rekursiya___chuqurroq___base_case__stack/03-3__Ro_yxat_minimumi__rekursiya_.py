def find(lst):
    if len(lst) == 1:
        return lst[0]
    sub = find(lst[1:])
    return lst[0] if lst[0] < sub else sub
numbers = list(map(int, input().split()))
print(find(numbers))