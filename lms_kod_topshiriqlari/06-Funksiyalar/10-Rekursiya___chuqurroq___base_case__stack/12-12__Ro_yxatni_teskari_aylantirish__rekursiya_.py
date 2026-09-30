def tes(lst):
    if not lst:
        return []
    return [lst[-1]] + tes(lst[:-1])
elem = input().split()
natija = tes(elem)
print(*natija)