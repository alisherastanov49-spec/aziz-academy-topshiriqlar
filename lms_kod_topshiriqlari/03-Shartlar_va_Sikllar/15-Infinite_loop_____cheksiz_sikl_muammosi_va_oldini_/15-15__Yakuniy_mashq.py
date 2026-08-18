import sys
lines = sys.stdin.read().splitlines()
if lines:
    first_line = lines[0].strip()
    if first_line.isdigit():
        n = int(first_line)
        numbers = list(map(int, lines[1].split()))
        firts = numbers[0]
        middle = numbers[1:-1]
        last = numbers[-1]
        print(firts)
        print(middle)
        print(last)
        
    else:
        for line in lines:
            if line.strip() == "stop":
                break
            print("Working")