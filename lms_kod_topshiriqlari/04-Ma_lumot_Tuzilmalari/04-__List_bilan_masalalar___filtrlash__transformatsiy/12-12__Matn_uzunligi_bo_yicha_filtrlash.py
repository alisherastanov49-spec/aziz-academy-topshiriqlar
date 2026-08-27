limit = int(input())
words = input().split()
result = [word for word in words if len(word) >= limit]
print(result)