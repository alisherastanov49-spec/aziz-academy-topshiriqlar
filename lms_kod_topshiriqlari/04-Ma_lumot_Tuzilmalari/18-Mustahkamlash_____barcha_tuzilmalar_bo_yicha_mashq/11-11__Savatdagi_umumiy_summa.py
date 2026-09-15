n = int(input())
savat = []
for _ in range(n):
    narx = int(input())
    soni = int(input())
    savat.append({'narx': narx, 'son': soni})
jami = sum(item['narx'] * item['son'] for item in savat)
print(jami)