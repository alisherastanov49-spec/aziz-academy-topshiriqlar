list1 = input().split()
list2 = input().split()
result = []
for item in list1:
    if item in list2 and item not in result:
        result.append(item)
print(" ".join(result))