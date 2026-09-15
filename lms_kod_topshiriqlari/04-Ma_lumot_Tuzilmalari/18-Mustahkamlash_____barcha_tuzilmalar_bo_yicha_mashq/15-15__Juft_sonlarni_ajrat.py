nums = list(map(int, input().split()))
evens = [x for x in nums if x % 2 == 0]
if evens:
    print(*evens)
else:
    print("yo'q")