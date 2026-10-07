def parse(line):
    return [int(x) for x in line.split()]
def line(items):
    return " ".join(str(x) for x in items)
nums = parse(input())
barobar = [x * 2 for x in nums]
print(line(barobar))