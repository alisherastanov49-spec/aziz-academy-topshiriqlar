items = input().split()
result = []

for val in items:
    try:
        result.append(int(val))
    except ValueError:
        try:
            result.append(float(val))
        except ValueError:
            result.append(val)
print(tuple(result))