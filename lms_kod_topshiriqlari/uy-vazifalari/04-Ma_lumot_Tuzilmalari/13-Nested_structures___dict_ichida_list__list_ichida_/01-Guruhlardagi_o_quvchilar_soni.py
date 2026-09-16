import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0].strip())
    groups = {}
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts:
            groups_name = parts[0]
            students = parts[1:]
            groups[groups_name] = students
    for group, students in groups.items():
        print(f"{group} {len(students)}")