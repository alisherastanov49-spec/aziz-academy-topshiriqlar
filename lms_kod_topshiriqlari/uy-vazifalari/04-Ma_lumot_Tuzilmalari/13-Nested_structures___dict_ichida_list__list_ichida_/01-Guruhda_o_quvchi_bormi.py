import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0].strip())
    groups = {}
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts:
            group_name = parts[0]
            students = parts[1:]
            groups[group_name] = students
    target_group, target_student = input_data[n + 1].split()
    if target_student in groups.get(target_group, []):
        print("Ha")
    else:
        print("Yoq")