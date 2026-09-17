import sys
from collections import Counter

nums = sys.stdin.read().split()
if nums:
    print(Counter(nums).most_common(1)[0][0])