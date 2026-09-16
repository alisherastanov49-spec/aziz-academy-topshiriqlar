import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0].strip())
    total_students = 0
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if len(parts) > 1:
            total_students += len(parts) - 1
    print(total_students)        