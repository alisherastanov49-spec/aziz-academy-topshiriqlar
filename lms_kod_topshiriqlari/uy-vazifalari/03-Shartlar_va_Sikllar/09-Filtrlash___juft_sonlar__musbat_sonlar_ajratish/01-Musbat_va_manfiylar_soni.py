n = int(input())
positives = 0
negatives = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
print(positives, negatives)