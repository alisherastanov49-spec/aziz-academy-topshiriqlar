import sys
input_data = sys.stdin.read().split()
if input_data:
    i = 0
    while i < len(input_data):
        amal = int(input_data[i])
        i += 1
        if amal == 0:
            break
        if amal not in [1, 2, 3, 4]:
            print("Noma'lum")
            continue
        a = int(input_data[i])
        b = int(input_data[i+1])
        i += 2
        if amal == 1:
            print(a + b)
        elif amal == 2:
            print(a - b)
        elif amal == 3:
            print(a * b)
        elif amal == 4:
            if b == 0:
                print("Xato")
            else:
                print(a // b)