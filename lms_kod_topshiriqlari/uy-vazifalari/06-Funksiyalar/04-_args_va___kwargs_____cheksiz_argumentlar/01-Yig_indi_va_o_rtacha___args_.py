def hisobot(*sonlar):
    yigindi = sum(sonlar)
    ortacha = yigindi // len(sonlar)
    return f"{yigindi} {ortacha}"
sonlar_list = list(map(int, input().split()))
print(hisobot(*sonlar_list))