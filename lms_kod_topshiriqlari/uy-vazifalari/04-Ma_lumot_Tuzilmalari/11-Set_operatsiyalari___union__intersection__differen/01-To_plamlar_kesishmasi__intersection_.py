set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
intersection_set = set1 & set2
print(*sorted(intersection_set))