import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0].strip())
    students_list = []
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts:
            name = parts[0]
            grades = [int(x) for x in parts[1:]]
            students_list.append({"name": name, "grades": grades})
    for student in students_list:
        print(f"{student['name']} {sum(student['grades'])}")