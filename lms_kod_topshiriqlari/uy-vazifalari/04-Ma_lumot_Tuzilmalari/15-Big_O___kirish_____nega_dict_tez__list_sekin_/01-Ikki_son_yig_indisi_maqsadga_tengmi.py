import sys
input_data = sys.stdin.read().splitlines()
if len(input_data) >= 2:
    nums = list(map(int, input_data[0].split()))
    target = int(input_data[1].strip())
    seen = set()
    found = False
    for x in nums:
        if (target - x) in seen:
            found = True
            break
        seen.add(x)
    if found:
        print("Ha")
    else:
        print("Yoq")