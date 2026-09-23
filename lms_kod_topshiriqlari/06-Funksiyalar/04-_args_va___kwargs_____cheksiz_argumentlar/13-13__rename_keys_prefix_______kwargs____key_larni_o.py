import sys 

lines = sys.stdin.read().splitlines()
prefix = lines[0]
n = int(lines[1])

print({prefix + parts[0]: int(parts[1]) for parts in [line.split() for line in lines[2:2+n]]})