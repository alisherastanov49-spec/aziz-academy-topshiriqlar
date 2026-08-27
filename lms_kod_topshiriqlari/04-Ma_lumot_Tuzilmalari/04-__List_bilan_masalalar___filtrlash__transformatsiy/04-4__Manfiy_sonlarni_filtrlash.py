n = input()
nums = [int(x) for x in input().split()]
negatives = [x for x in nums if x < 0]
print(negatives)