import sys
input_data = sys.stdin.read().splitlines()
if len(input_data) >= 2:
    set1 = set(map(int, input_data[0].split()))
    set2 = set(map(int, input_data[1].split()))
    common = sorted(set1 & set2)
    print(*common)