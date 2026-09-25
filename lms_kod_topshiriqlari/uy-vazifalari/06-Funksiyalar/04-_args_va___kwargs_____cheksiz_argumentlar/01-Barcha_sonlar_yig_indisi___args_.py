def yigindi(*sonlar):
    return sum(sonlar)
sonlar_list = list(map(int, input().split()))
print(yigindi(*sonlar_list))