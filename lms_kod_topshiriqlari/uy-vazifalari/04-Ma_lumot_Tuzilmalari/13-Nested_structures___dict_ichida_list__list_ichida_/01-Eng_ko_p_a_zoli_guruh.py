import  sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0].strip())
    max_group = ""
    max_count = -1
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts:
            group_name = parts[0]
            students_count = len(parts[1:])
            if students_count > max_count:
                max_count = students_count
                max_group = group_name
    print(max_group)          