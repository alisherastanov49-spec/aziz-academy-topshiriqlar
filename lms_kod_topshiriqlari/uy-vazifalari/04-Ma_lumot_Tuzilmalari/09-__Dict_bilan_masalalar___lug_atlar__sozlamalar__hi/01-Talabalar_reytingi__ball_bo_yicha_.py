n = int(input())
students = {}
for _ in range(n):
    name, score = input().split()
    students[name]  = int(score)
sorted_students = sorted(students.items(), key=lambda x: (-x[1], x[0]))
for name, score in sorted_students:
    print(f"{name} {score}")