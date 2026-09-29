def per(eni, boyi):
    return 2 * (eni + boyi)
def yuzi(eni, boyi):
    return eni * boyi
eni, boyi = map(int, input().split())
print(per(eni, boyi))
print(yuzi(eni, boyi))