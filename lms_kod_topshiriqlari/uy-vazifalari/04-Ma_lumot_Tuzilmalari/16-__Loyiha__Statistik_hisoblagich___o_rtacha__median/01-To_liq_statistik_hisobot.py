import sys, statistics as st
nums = sorted(map(int, sys.stdin.read().split()))
print(f"O'rtacha: {float(round(st.mean(nums), 2))}\nMediana: {st.median_low(nums)}\nModa: {st.multimode(nums)[0]}")