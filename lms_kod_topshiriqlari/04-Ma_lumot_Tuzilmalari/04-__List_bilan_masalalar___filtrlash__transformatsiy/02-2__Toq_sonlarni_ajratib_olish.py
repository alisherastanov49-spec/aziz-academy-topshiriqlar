n = input()
nums = [int(x) for x in input().split()]
odds = [x for x in nums if x % 2 != 0]
print(odds)