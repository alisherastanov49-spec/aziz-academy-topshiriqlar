from collections import Counter
words = input().split()
print(Counter(words).most_common(1)[0][0])
