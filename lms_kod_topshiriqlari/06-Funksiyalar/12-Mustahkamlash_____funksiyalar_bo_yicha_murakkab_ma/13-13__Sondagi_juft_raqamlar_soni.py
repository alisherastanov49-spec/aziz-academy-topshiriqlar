s = input()
print(sum(1 for ch in s if ch.isdigit() and int(ch) % 2 == 0))