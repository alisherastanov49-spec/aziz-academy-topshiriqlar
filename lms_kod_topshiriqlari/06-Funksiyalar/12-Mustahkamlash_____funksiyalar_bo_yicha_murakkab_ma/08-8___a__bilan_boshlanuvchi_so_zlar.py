words = input().split()
count = sum(1 for word in words if word.lower().startswith('a'))
print(count)