from collections import Counter
sonlar = input().split()
sanoq = Counter(sonlar)
print(sum(1 for v in sanoq.values() if v > 1))
