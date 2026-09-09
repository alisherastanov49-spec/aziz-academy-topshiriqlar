s = input().strip()
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
max_char = None
max_count = -1
for char in s:
    if counts[char] > max_count:
        max_count = counts[char]
        max_char = char
print(max_char)