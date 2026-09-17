import sys
from collections import Counter
items = sys.stdin.read().split()
if items:
    counts = Counter(items)
    most_common_item = counts.most_common(1)[0][0]
    print(most_common_item)