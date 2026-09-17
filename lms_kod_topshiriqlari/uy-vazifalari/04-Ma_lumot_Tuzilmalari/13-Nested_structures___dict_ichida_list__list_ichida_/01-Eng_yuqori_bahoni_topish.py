import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    lines = [line.strip() for line in input_data if line.strip()]
    if lines:
        n = int(lines[0])
        students = []
        for i in range(1, n + 1):
            parts = lines[i].split()
            name = parts[0]
            grades = list(map(int, parts[1:]))
            students.append({"ism": name, "baholar": grades})
        max_grade = float("-inf")
        top_student = ""
        for student in students:
            for grade in student["baholar"]:
                if grade > max_grade:
                    max_grade = grade
                    top_student = student["ism"]
        print(f"{top_student} {max_grade}")