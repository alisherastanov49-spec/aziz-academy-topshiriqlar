import sys
input_data = sys.stdin.read().splitlines()
if len(input_data) >= 2:
    elements = set(input_data[0].split())
    target = input_data[1].strip()
    if target in elements:
        print("Ha")
    else:
        print("Yoq")