nums = list(map(int, input().split()))
positives = [x for x in nums if x > 0]
print(min(positives))