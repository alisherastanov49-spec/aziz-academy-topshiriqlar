def baho(ball):
    if ball >= 90:
        return "A"
    if ball >= 80:
        return "B"
    if ball >= 70:
        return "C"
    if ball >= 60:
        return "D"
    return "F"
def otdimi(ball):
    if ball >= 60:
        return "otdi"
    return "yiqildi"
ball = int(input())
print(baho(ball))
print(otdimi(ball))