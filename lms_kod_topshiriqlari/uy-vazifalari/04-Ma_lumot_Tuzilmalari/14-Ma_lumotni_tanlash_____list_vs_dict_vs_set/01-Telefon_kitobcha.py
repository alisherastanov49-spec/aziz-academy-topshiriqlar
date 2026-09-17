import sys
data = sys.stdin.read().split()
n = int(data[0])
phone_book = dict(zip(data[1 : 2 * n + 1 : 2], data[2 : 2 * n + 1 : 2]))
for name in data[2 * n + 2 :]:
    print(phone_book.get(name, "topilmadi"))